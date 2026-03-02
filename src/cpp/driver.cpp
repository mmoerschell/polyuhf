#include <cstddef>
#include <cstdint>
#include <cstring>

#include <print>
#include <string>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using boost::multiprecision::export_bits;
using boost::multiprecision::import_bits;

#define LIMBS 6
#define LAMBDA 25
#define LAMBDA_MASK ((1ull << LAMBDA) - 1)

typedef struct {
    uint64_t limbs[LIMBS];
} bigint_t;

void print_vec(const std::vector<uint8_t> &v) {
    for (auto b : v)
        std::print("{}, ", b);
    std::println();
}

void print_bigint(const bigint_t &x) {
    for (const auto limb : x.limbs)
        std::print("{}, ", limb);
    std::println();
}

bigint_t from_boost(const cpp_int &x) {
    // Export bits
    std::vector<uint8_t> bits{}; // little-endian
    export_bits(x, std::back_inserter(bits), 1, false);
    // Create limbs
    bigint_t result{};
    for (size_t i = 0; i < LIMBS; ++i) {
        size_t base = i * LAMBDA; // first bit index of this limb
        for (size_t j = 0; j < LAMBDA; ++j) {
            const size_t bit_index = base + j;
            if (bit_index < bits.size() && bits[bit_index])
                result.limbs[i] |=
                    static_cast<uint64_t>(1ull << j); // set bit j in the limb
        }
    }
    return result;
}

cpp_int to_boost(const bigint_t &b) {
    std::vector<uint8_t> bits{}; // little-endian
    for (auto limb : b.limbs)
        for (size_t j = 0; j < LAMBDA; ++j)
            bits.push_back((limb >> j) & 1ull);
    cpp_int x{};
    import_bits(x, bits.cbegin(), bits.cend(), 1, false);
    return x;
}

void carry_round(bigint_t *x) {
    for (int32_t i = 0; i < LIMBS - 1; ++i) {
        const auto carry_amount = x->limbs[i] >> LAMBDA;
        x->limbs[i] &= LAMBDA_MASK;
        x->limbs[i + 1] += carry_amount;
    }
    // TODO: field arithmetic, carry last limb back to first?
}

void add(const bigint_t *a, const bigint_t *b, bigint_t *result) {
    for (int i = 0; i < LIMBS; ++i)
        result->limbs[i] = a->limbs[i] + b->limbs[i];
    carry_round(result);
}

void mul(const bigint_t *a, const bigint_t *b, bigint_t *result) {
    std::memset(result, 0, sizeof(bigint_t));
    for (size_t i = 0; i < LIMBS; ++i) {
        for (size_t j = 0; j <= i; ++j) {
            result->limbs[i] += a->limbs[j] * b->limbs[i - j];
        }
    }
    carry_round(result);
}

bigint_t _bigint_add(bigint_t a, bigint_t b) {
    bigint_t result;
    add(&a, &b, &result);
    return result;
}

bigint_t _bigint_mul(bigint_t a, bigint_t b) {
    bigint_t result;
    mul(&a, &b, &result);
    return result;
}

bigint_t mmh(bigint_t *R, bigint_t *M, int64_t n) {
    bigint_t _1_acc = {0b00, 0b0, 0b0, 0b0, 0b0, 0b0};
    int64_t i = 0;
    while (((i) < (((n) - (1))))) {
        _1_acc = _bigint_add(_1_acc, _bigint_add(M[i], R[i]));
        i = ((i) + (1));
    }
    return _bigint_add(_1_acc, M[((n) - (1))]);
}
int main(int argc, char **argv) {
    // Some random numbers
    const std::string a = "349960181123123123123123123123184565089498273"
                          "82974658930387575987190014771576210832368861184";
    const std::string b = "1231231233434343434445454545545677";
    // const std::string a = "100000000000000000000999999000000", b = "1232";
    // const std::string a = "1231231230099999", b = "1232789789789";

    // Boost MP
    const cpp_int mp_a(a);
    const cpp_int mp_b(b);
    const cpp_int mp_sum = mp_a + mp_b;
    const cpp_int mp_prod = mp_a * mp_b;

    // Code under test
    bigint_t cu_a = from_boost(mp_a), cu_b = from_boost(mp_b), cu_sum, cu_prod;
    add(&cu_a, &cu_b, &cu_sum);
    mul(&cu_a, &cu_b, &cu_prod);
    std::println("{}", mp_sum.convert_to<std::string>());
    std::println("{}", to_boost(cu_sum).convert_to<std::string>());
    std::println("{}", mp_prod.convert_to<std::string>());
    std::println("{}", to_boost(cu_prod).convert_to<std::string>());

    // MMH
    constexpr size_t N = 10;
}
