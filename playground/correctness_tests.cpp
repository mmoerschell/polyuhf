#include "gmock/gmock.h"
#include <cstddef>
#include <cstdint>
#include <cstring>

#include <array>
#include <iomanip>
#include <print>
#include <span>
#include <stdexcept>

#include <arm_neon.h>

#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <tuple>
#include <vector>

#include "datastructures.h"
#include "field_arithmetic.h"
#include "sbox.h"
#include "mmh.h"

using ::testing::ElementsAreArray;

#define SIMD_WIDTH 2ull

void parse_hex(const std::string &hex, std::span<uint8_t> data) {
    if (data.size() * 2 != hex.size())
        throw std::runtime_error(
            std::format("Hex size {} does not match buffer size {}", hex.size(),
                        data.size()));
    auto hex_it = hex.cbegin();
    auto data_it = data.begin();
    while (hex_it < hex.cend() && data_it < data.end()) {
        uint8_t byte = 0;
        for (size_t i = 0; i < 2; ++i) {
            uint8_t nibble = *(hex_it + i);
            if (nibble >= 'A' && nibble <= 'Z')
                nibble = nibble - 'A' + 10;
            else if (nibble >= 'a' && nibble <= 'z')
                nibble = nibble - 'a' + 10;
            else if (nibble >= '0' && nibble <= '9')
                nibble -= '0';
            else
                throw std::runtime_error(
                    std::format("Invalid hex char {:d}", nibble));
            byte |= nibble << ((1 - i) * 4);
        }
        hex_it += 2;
        *(data_it++) = byte;
    }
}

inline std::string to_hex(std::span<uint8_t> v) {
    std::ostringstream oss;
    oss << std::hex << std::setfill('0');

    for (auto b : v) {
        oss << std::setw(2) << static_cast<uint64_t>(b) << ' ';
    }
    return oss.str();
}

TEST(ParsingTests, ParseDeadBeef) {
    std::array<uint8_t, 4> actual{}, expected = {0xde, 0xad, 0xbe, 0xef};
    parse_hex("deadbeef", actual);
    EXPECT_THAT(actual, ElementsAreArray(expected));
}

TEST(LoadingTests, LoadZeroes) {
    const std::vector<uint8_t> bytes(14, 0);
    bigint_t x;
    load_le_bytes(&x, bytes.data(), bytes.size());
    EXPECT_THAT(std::span<uint64_t>(x.limbs, LIMBS),
                ElementsAreArray(std::vector<uint64_t>(LIMBS, 0ull)));
}

TEST(LoadingTests, LoadOnes) {
    const std::vector<uint8_t> bytes(14, 0xff);
    bigint_t x;
    load_le_bytes(&x, bytes.data(), bytes.size());
    carry_round(&x);
    EXPECT_THAT(
        std::span<uint64_t>(x.limbs, LIMBS - 1),
        ElementsAreArray(std::vector<uint64_t>(LIMBS - 1, LAMBDA_MASK)));
    EXPECT_EQ(x.limbs[LIMBS - 1], (1ull << 16) - 1ull);
}

TEST(ArithmeticTests, SimpleSum) {
    bigint_t a, b, c;
    load_le_bytes(&a, SBOX, 14);
    load_le_bytes(&b, &SBOX[14], 14);
    memset(&c, 0, sizeof(c));
    op_add(&c, &a, &b);
    carry_round(&c);

    std::array<uint8_t, 15> sum_act{}, sum_exp{};
    parse_hex("0ef341febbe9691f78f11400a18701", sum_exp);

    store_le_bytes(sum_act.data(), sum_act.size(), &c);
    EXPECT_EQ(memcmp(sum_act.data(), sum_exp.data(), sum_act.size()), 0)
        << "\nact: " << to_hex(sum_act) << "\nexp: " << to_hex(sum_exp);
}

TEST(ArithmeticTests, BasicSboxSum) {
    bigint_t acc, current;
    memset(&acc, 0, sizeof(acc));

    for (size_t i = 0; i < 18; ++i) {
        load_le_bytes(&current, SBOX + 14 * i, 14);
        op_add(&acc, &acc, &current);
    }
    load_le_bytes(&current, SBOX + 14 * 18, 4);
    op_add(&acc, &acc, &current);
    carry_round(&acc);

    std::array<uint8_t, 15> tag_act{}, tag_exp{};
    parse_hex("b4d2ec186e6319f9cd9792679e860a", tag_exp);

    store_le_bytes(tag_act.data(), tag_act.size(), &acc);
    EXPECT_EQ(memcmp(tag_act.data(), tag_exp.data(), tag_act.size()), 0)
        << "\nact: " << to_hex(tag_act) << "\nexp: " << to_hex(tag_exp);
}

TEST(VectorTests, BasicSboxSum) {
    // Solution
    std::array<uint8_t, 15> tag_act{}, tag_exp{};
    parse_hex("b4d2ec186e6319f9cd9792679e860a", tag_exp);

    // Implementation
    alignas(64) uint64x2_t acc[LIMBS] = {0};

    for (size_t pass = 0; pass < 9; ++pass) {
        // Load 2 bigints into current
        alignas(64) uint64x2_t current[LIMBS];
        for (size_t row = 0; row < LIMBS - 1; ++row) {
            current[row] = {
                (static_cast<uint64_t>(SBOX[28 * pass + 3 * row])) |
                    (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 1])
                     << 8ull) |
                    (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 2])
                     << 16ull),
                (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 14])) |
                    (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 15])
                     << 8ull) |
                    (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 16])
                     << 16ull)};
        }
        current[LIMBS - 1] = {
            (static_cast<uint64_t>(SBOX[28 * pass + 12])) |
                (static_cast<uint64_t>(SBOX[28 * pass + 13]) << 8ull),
            (static_cast<uint64_t>(SBOX[28 * pass + 26])) |
                (static_cast<uint64_t>(SBOX[28 * pass + 27]) << 8ull)};

        // acc = limb-wise sum of acc and current
        for (size_t i = 0; i < LIMBS; ++i)
            acc[i] = vaddq_u64(acc[i], current[i]);
    }

    // Horizontal reduction
    bigint_t result;
    for (size_t i = 0; i < LIMBS; ++i)
        result.limbs[i] = vaddvq_u64(acc[i]);

    // Missing data
    bigint_t tmp;
    load_le_bytes(&tmp, SBOX + 252, 4);
    op_add(&result, &result, &tmp);

    // Carry
    carry_round(&result);

    // Export
    store_le_bytes(tag_act.data(), tag_act.size(), &result);

    EXPECT_EQ(memcmp(tag_act.data(), tag_exp.data(), tag_act.size()), 0)
        << "\nact: " << to_hex(tag_act) << "\nexp: " << to_hex(tag_exp);
}

typedef std::tuple<uint64_t, uint64_t, size_t, const std::string>
    hash_function_input;
class HashingTest : public testing::TestWithParam<hash_function_input> {
  protected:
    HashingTest() {
        const auto [message_seed, key_seed, size, tag] = GetParam();

        message_.resize(size);
        key_.resize(size);

        deterministic_sequence(message_seed, message_);
        deterministic_sequence(key_seed, key_);
    }

    ~HashingTest() override = default;

    std::vector<uint8_t> message_;
    std::vector<uint8_t> key_;

  public:
    static void deterministic_sequence(const uint64_t seed,
                                       std::span<uint8_t> data) {
        for (size_t i = 0; i < data.size(); ++i)
            data[i] =
                static_cast<uint8_t>((i * seed >> 24) ^ (i & 1 ? 0xaa : 0x55));
    }

    static void print_buffer(const std::span<uint8_t> data) {
        for (size_t i = 0; i < data.size(); ++i)
            std::print("{:02x} ", data[i]);
        std::println("");
    }
};

TEST_P(HashingTest, Scalar) {
    // Params, input, solution
    const auto [message_seed, key_seed, size, tag_hex] = GetParam();
    const auto tag_size = tag_hex.size() / 2;
    std::vector<uint8_t> tag_act(tag_size, 0), tag_exp(tag_size, 0);
    parse_hex(tag_hex, tag_exp);

    // Compute
    bigint_t acc, Mi, ri, product;
    memset(&acc, 0, sizeof(acc));
    const uint64_t B =
        (size + BYTES_PER_FIELD_ELEMENT - 1ull) / BYTES_PER_FIELD_ELEMENT;
    for (size_t i = 0; i < B - 1; ++i) {
        memset(&Mi, 0, sizeof(Mi));
        memset(&ri, 0, sizeof(ri));
        memset(&product, 0, sizeof(product));
        load_le_bytes(&Mi, message_.data() + BYTES_PER_FIELD_ELEMENT * i,
                      BYTES_PER_FIELD_ELEMENT);
        load_le_bytes(&ri, key_.data() + BYTES_PER_FIELD_ELEMENT * i,
                      BYTES_PER_FIELD_ELEMENT);
        op_mul(&product, &Mi, &ri);
        op_add(&acc, &acc, &product);
    }
    memset(&Mi, 0, sizeof(Mi));
    load_le_bytes(&Mi, message_.data() + BYTES_PER_FIELD_ELEMENT * (B - 1),
                  size % BYTES_PER_FIELD_ELEMENT);
    op_add(&acc, &acc, &Mi);

    // Carry
    carry_round(&acc);

    // Store
    store_le_bytes(tag_act.data(), tag_act.size(), &acc);

    // Check
    EXPECT_EQ(memcmp(tag_act.data(), tag_exp.data(), tag_act.size()), 0)
        << "\nact: " << to_hex(tag_act) << "\nexp: " << to_hex(tag_exp);
}

uint64x2_t vmulq_u64(uint64x2_t a, uint64x2_t b) {
    // 1. Multiply the low 32 bits: (A_lo * B_lo)
    // vmovn_u64 extracts the lower 32 bits of each 64-bit lane.
    // vmull_u32 multiplies those 32-bit values into 64-bit results.
    uint64x2_t lo_mul = vmull_u32(vmovn_u64(a), vmovn_u64(b));

    // 2. Prepare for cross-term multiplication
    // Reinterpret as 32-bit vectors to manipulate the halves.
    uint32x4_t a32 = vreinterpretq_u32_u64(a);
    uint32x4_t b32 = vreinterpretq_u32_u64(b);

    // vrev64q_u32 swaps the high and low 32-bit words within each 64-bit lane.
    // So if a32 is [A_lo, A_hi], a_rev becomes [A_hi, A_lo].
    uint32x4_t a_rev = vrev64q_u32(a32);

    // 3. Compute cross terms: [A_hi * B_lo, A_lo * B_hi]
    uint32x4_t cross_mul = vmulq_u32(a_rev, b32);

    // 4. Add the cross terms together: (A_hi * B_lo) + (A_lo * B_hi)
    // Swapping cross_mul gives [A_lo * B_hi, A_hi * B_lo]
    uint32x4_t cross_sum = vaddq_u32(cross_mul, vrev64q_u32(cross_mul));

    // 5. Shift the cross terms into the upper 32 bits.
    // By casting back to 64-bit and shifting left by 32, the lower 32 bits of
    // the cross_sum move to the upper half, and the lower half becomes 0.
    uint64x2_t cross_shifted =
        vshlq_n_u64(vreinterpretq_u64_u32(cross_sum), 32);

    // 6. Add the shifted cross terms to the low multiplication
    return vaddq_u64(lo_mul, cross_shifted);
}

TEST(ARMExtensions, Multiplication) {
    const auto x = 0x5555555555555555ull, y = 0xaaaaaaaaaaaaaaaaull;
    uint64x2_t a = {x, y};
    uint64x2_t b = {2, 2};
    auto c = vmulq_u64(a, b);
    auto x_prime = vgetq_lane_u64(c, 0);
    auto y_prime = vgetq_lane_u64(c, 1);
    EXPECT_EQ(x_prime, x << 1ull);
    EXPECT_EQ(y_prime, y << 1ull);
}

TEST(ARMExtensions, RandomMultiplication) {
    const uint64_t N = 100;
    const uint64_t bound = 1ull << 63;
    for (uint64_t x1 = bound - N + 1; x1 <= bound; ++x1) {
        for (uint64_t y1 = bound - N + 1; y1 <= bound; ++y1) {
            for (uint64_t x2 = bound - N + 1; x2 <= bound; ++x2) {
                for (uint64_t y2 = bound - N + 1; y2 <= bound; ++y2) {
                    uint64x2_t v1{x1, y1};
                    uint64x2_t v2{x2, y2};
                    auto res = vmulq_u64(v1, v2);
                    uint64_t data[2];
                    vst1q_u64(data, res);
                    EXPECT_EQ(data[0], x1 * x2);
                    EXPECT_EQ(data[1], y1 * y2);
                }
            }
        }
    }
}

// Loading helper
void load(uint8_t *src, uint64x2_t *dst) {
    for (size_t row = 0; row < LIMBS - 1; ++row) {
        dst[row] = {(static_cast<uint64_t>(src[3 * row + 0])) |
                        (static_cast<uint64_t>(src[3 * row + 1]) << 8ull) |
                        (static_cast<uint64_t>(src[3 * row + 2]) << 16ull),
                    (static_cast<uint64_t>(src[3 * row + 14])) |
                        (static_cast<uint64_t>(src[3 * row + 15]) << 8ull) |
                        (static_cast<uint64_t>(src[3 * row + 16]) << 16ull)};
    }
    dst[LIMBS - 1] = {(static_cast<uint64_t>(src[12])) |
                          (static_cast<uint64_t>(src[13]) << 8ull),
                      (static_cast<uint64_t>(src[26])) |
                          (static_cast<uint64_t>(src[27]) << 8ull)};
};

TEST_P(HashingTest, Vector) {
    // Params, input, solution
    const auto [message_seed, key_seed, size, tag_hex] = GetParam();
    const auto tag_size = tag_hex.size() / 2;
    std::vector<uint8_t> tag_act(tag_size, 0), tag_exp(tag_size, 0);
    parse_hex(tag_hex, tag_exp);
    ASSERT_EQ(size, message_.size());

    // Compute
    alignas(64) uint64x2_t acc[LIMBS] = {0};
    alignas(64) uint64x2_t Mi[LIMBS] = {0};
    alignas(64) uint64x2_t ri[LIMBS] = {0};

    // Count field elements
    const uint64_t B = (size + BYTES_PER_FIELD_ELEMENT - 1ull) /
                       BYTES_PER_FIELD_ELEMENT; // Total
    const uint64_t n_vector_passes = (B - 1) / SIMD_WIDTH;

    // Vectorized loop
    for (size_t pass = 0; pass < n_vector_passes; ++pass) {
        // Load
        load(message_.data() + SIMD_WIDTH * BYTES_PER_FIELD_ELEMENT * pass, Mi);
        load(key_.data() + SIMD_WIDTH * BYTES_PER_FIELD_ELEMENT * pass, ri);

        // Product
        alignas(64) uint64x2_t product[LIMBS]{};
        for (size_t i = 0; i < LIMBS; ++i) {
            for (size_t j = 0; j <= i; ++j)
                product[i] = vaddq_u64(product[i], vmulq_u64(Mi[j], ri[i - j]));
            // dst.limbs[i] += lhs.limbs[j] * rhs.limbs[i - j];
            for (size_t j = i + 1; j < LIMBS; ++j)
                product[i] = vaddq_u64(
                    product[i],
                    vmulq_u64(vmulq_u64(Mi[j], uint64x2_t{KAPPA, KAPPA}),
                              ri[LIMBS + i - j]));
            // dst.limbs[i] += lhs.limbs[j] * KAPPA * rhs.limbs[LIMBS + i - j];
        }

        // Addition
        for (size_t i = 0; i < LIMBS; ++i)
            acc[i] = vaddq_u64(acc[i], product[i]);
    }

    // Horizontal reduction
    bigint_t result;
    for (size_t i = 0; i < LIMBS; ++i)
        result.limbs[i] = vaddvq_u64(acc[i]);

    // Missing data
    for (size_t i = n_vector_passes * SIMD_WIDTH; i < B - 1; ++i) {
        // Load
        // Add
        std::println("Missing data!!");
    }

    // Last message field element (M[B])
    bigint_t tmp;
    memset(&tmp, 0, sizeof(tmp));
    load_le_bytes(&tmp, message_.data() + (B - 1) * BYTES_PER_FIELD_ELEMENT,
                  message_.size() % BYTES_PER_FIELD_ELEMENT);
    op_add(&result, &result, &tmp);

    // Carry
    carry_round(&result);

    // Export
    store_le_bytes(tag_act.data(), tag_act.size(), &result);

    // Check
    EXPECT_EQ(memcmp(tag_act.data(), tag_exp.data(), tag_act.size()), 0)
        << "\nact: " << to_hex(tag_act) << "\nexp: " << to_hex(tag_exp);
}

TEST_P(HashingTest, TheRealMMH) {
    // Params, input, solution
    const auto [message_seed, key_seed, size, tag_hex] = GetParam();
    const auto tag_size = tag_hex.size() / 2;
    std::vector<uint8_t> tag_act(tag_size, 0), tag_exp(tag_size, 0);
    parse_hex(tag_hex, tag_exp);
    ASSERT_EQ(size, message_.size());

    const uint64_t B = (size + BYTES_PER_FIELD_ELEMENT - 1ull) /
                       BYTES_PER_FIELD_ELEMENT; // Total
    // const uint64_t B = 1;
    auto result = mmh(message_.data(), key_.data(), B);
    auto lambd = 24;
    auto limbs = 5;
    // Store
    for (size_t i = 0; i < tag_act.size(); ++i) {
        const size_t global_bit_idx = 8 * i;
        const size_t limb_idx = global_bit_idx / lambd;
        const size_t local_bit_idx = global_bit_idx % lambd;
        tag_act.data()[i] |= (uint8_t)(result.limbs[limb_idx] >> local_bit_idx);
        // if (limb_idx + 1 < limbs) {
        //     tag_act.data()[i] |=
        //         (uint8_t)(result.limbs[limb_idx + 1] << (lambd - local_bit_idx));
        // }
    }
    // Check
    EXPECT_EQ(memcmp(tag_act.data(), tag_exp.data(), tag_act.size()), 0)
        << "\nact: " << to_hex(tag_act) << "\nexp: " << to_hex(tag_exp);
}

const std::vector<hash_function_input> mmh_tests = {
    {0xbaadf00dull, 0xcafebabeull, 16000ull, "4041c098959e745e51764e6e9edf0e"},
    {0xdeadbeefull, 0xfeedfaceull, 16000ull, "bad7acaaa0fe664421a631317edb0e"},
    {0xbaadc0deull, 0xfacefeedull, 16000ull, "09844874fe87c5e4a7fca9ea6aa80c"},
};

INSTANTIATE_TEST_SUITE_P(MMH_Hashing, HashingTest,
                         testing::ValuesIn(mmh_tests));

TEST(VectorizedMultiplicationTests, Simple) {
    std::vector<uint8_t> message(28), key(28);
    HashingTest::deterministic_sequence(0xbaadf00dull, message);
    HashingTest::deterministic_sequence(0xcafebabeull, key);
    uint64x2_t M12[LIMBS] = {0}, r12[LIMBS] = {0};
    load(message.data(), M12);
    load(key.data(), r12);
    alignas(64) uint64x2_t product[LIMBS]{};
    for (size_t i = 0; i < LIMBS; ++i) {
        for (size_t j = 0; j <= i; ++j)
            product[i] = vaddq_u64(product[i], vmulq_u64(M12[j], r12[i - j]));
        for (size_t j = i + 1; j < LIMBS; ++j)
            product[i] =
                vaddq_u64(product[i],
                          vmulq_u64(vmulq_u64(M12[j], uint64x2_t{KAPPA, KAPPA}),
                                    r12[LIMBS + i - j]));
    }
    // Horizontal reduction
    bigint_t result;
    for (size_t i = 0; i < LIMBS; ++i)
        result.limbs[i] = vaddvq_u64(product[i]);
    carry_round(&result);
    std::array<uint8_t, 15> tag{};
    store_le_bytes(tag.data(), tag.size(), &result);
    // HashingTest::print_buffer(tag);

    // Solution, check
    std::array<uint8_t, 15> solution{};
    parse_hex("74566862fc81c42959e647bc889e0d", solution);
    EXPECT_EQ(memcmp(tag.data(), solution.data(), tag.size()), 0)
        << "\nact: " << to_hex(tag) << "\nexp: " << to_hex(solution);
}
