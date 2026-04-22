#include "gmock/gmock.h"
#include <cstdint>
#include <cstring>

#include <array>
#include <iomanip>
#include <span>
#include <stdexcept>

#include <arm_neon.h>

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "datastructures.h"
#include "field_arithmetic.h"
#include "sbox.h"

using ::testing::ElementsAreArray;

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
                (static_cast<uint64_t>(SBOX[28 * pass + 3 * row])) | (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 1]) << 8ull) | (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 2]) << 16ull),
                (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 14])) | (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 15]) << 8ull) | (static_cast<uint64_t>(SBOX[28 * pass + 3 * row + 16]) << 16ull)
            };
        }
        current[LIMBS - 1] = {
                (static_cast<uint64_t>(SBOX[28 * pass + 12])) | (static_cast<uint64_t>(SBOX[28 * pass + 13]) << 8ull),
                (static_cast<uint64_t>(SBOX[28 * pass + 26])) | (static_cast<uint64_t>(SBOX[28 * pass + 27]) << 8ull)
        };

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
