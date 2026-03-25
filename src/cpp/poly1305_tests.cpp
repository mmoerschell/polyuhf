#include <array>
#include <cstddef>
#include <cstdint>
#include <cstring>
#include <numeric>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::multiprecision;
namespace bdata = boost::unit_test::data;

#include <openssl/evp.h>

#include "poly1305_testcases_loader.hpp"

#include "generated/poly1305.h"

static const std::vector<TestCase> tests =
    load_tests_from_file("src/cpp/poly1305-rfc-test-vectors.json");

void poly1305_wrapper(uint8_t *tag, const uint8_t *key, const uint8_t *message,
                      const size_t message_size) {
    auto r = from_le_bytes(key, 16);
    std::vector<bigint_t> blocks;
    for (size_t i = 0; i < message_size; i += 16)
        blocks.push_back(from_le_bytes(message + i, 16));
    auto dsl_tag = poly1305(r, blocks.data(), blocks.size());
    cpp_int polynomial_part, s_helper, sixteen_byte_sum;
    import_bits(polynomial_part, dsl_tag.limbs, dsl_tag.limbs + LIMBS, LAMBDA,
                false);
    import_bits(s_helper, key + 16, key + 32, 8, false);
    sixteen_byte_sum = (polynomial_part + s_helper) &
                       cpp_int("0xffffffffffffffffffffffffffffffff");
    memset(tag, 0, 16);
    export_bits(sixteen_byte_sum, tag, 8, false);
}

BOOST_AUTO_TEST_CASE(TestByteLoadingUnloading) {
    // c = a * b % (2^130-5)
    std::array<uint8_t, 16> data_a = {0x4c, 0x32, 0x46, 0x3f, 0xa3, 0x55,
                                      0x25, 0xd7, 0x68, 0x33, 0x1b, 0x12,
                                      0x41, 0xe1, 0x0c, 0x5b};
    std::array<uint8_t, 16> data_b = {0x59, 0x9c, 0x0e, 0xa0, 0x2d, 0x45,
                                      0x52, 0x30, 0x5d, 0x59, 0x58, 0xc7,
                                      0xe9, 0xe0, 0xd0, 0xe3};
    std::array<uint8_t, 17> data_c = {0xb4, 0x13, 0xc1, 0x1d, 0xe4, 0x13,
                                      0xc6, 0x79, 0x79, 0x8f, 0x33, 0x8e,
                                      0x27, 0x03, 0xbf, 0x44, 0x02};

    // Loading, mul
    const auto a = from_le_bytes(data_a.data(), data_a.size());
    const auto b = from_le_bytes(data_b.data(), data_b.size());
    const auto c_ref = from_le_bytes(data_c.data(), data_c.size());
    const auto c = _bigint_mul(a, b);
    BOOST_CHECK_EQUAL_COLLECTIONS(c.limbs, c.limbs + LIMBS, c_ref.limbs,
                                  c_ref.limbs + LIMBS);

    // Unloading
    std::array<uint8_t, 16> data_a_prime, data_b_prime;
    std::array<uint8_t, 17> data_c_prime;
    to_le_bytes(data_a_prime.data(), data_a_prime.size(), &a);
    to_le_bytes(data_b_prime.data(), data_b_prime.size(), &b);
    to_le_bytes(data_c_prime.data(), data_c_prime.size(), &c_ref);
    BOOST_CHECK_EQUAL_COLLECTIONS(data_a_prime.cbegin(), data_a_prime.cend(),
                                  data_a.cbegin(), data_a.cend());
    BOOST_CHECK_EQUAL_COLLECTIONS(data_b_prime.cbegin(), data_b_prime.cend(),
                                  data_b.cbegin(), data_b.cend());
    BOOST_CHECK_EQUAL_COLLECTIONS(data_c_prime.cbegin(), data_c_prime.cend(),
                                  data_c.cbegin(), data_c.cend());
}

BOOST_DATA_TEST_CASE(RFC_Test_Vectors, bdata::make(tests), tc) {
    // Validate RFC testcases against OpenSSL
    // Checks for typos & other issues
    alignas(64) std::array<uint8_t, 16> openssl_tag;
    std::iota(openssl_tag.begin(), openssl_tag.end(),
              42); // fill with non-zero data

    EVP_MAC *mac = EVP_MAC_fetch(nullptr, "POLY1305", nullptr);
    EVP_MAC_CTX *ctx = EVP_MAC_CTX_new(mac);

    OSSL_PARAM params[] = {
        // Assuming OpenSSL does not write to the key
        OSSL_PARAM_construct_octet_string(
            "key", const_cast<uint8_t *>(tc.key.data()), tc.key.size()),
        OSSL_PARAM_END};

    EVP_MAC_init(ctx, nullptr, 0, params);
    EVP_MAC_update(ctx, tc.message.data(), tc.message.size());
    size_t tag_len = openssl_tag.size();
    EVP_MAC_final(ctx, openssl_tag.data(), &tag_len, tag_len);
    EVP_MAC_CTX_free(ctx);
    EVP_MAC_free(mac);
    BOOST_REQUIRE_EQUAL(tag_len, 16);

    BOOST_CHECK_EQUAL_COLLECTIONS(openssl_tag.cbegin(), openssl_tag.cend(),
                                  tc.tag.cbegin(), tc.tag.cend());

    // If message length is a multiple of 16, test DSL implementation
    if ((tc.message.size() & 15) == 0) {
        std::array<uint8_t, 16> tag_bytes{};
        poly1305_wrapper(tag_bytes.data(), tc.key.data(), tc.message.data(),
                         tc.message.size());
        BOOST_CHECK_EQUAL_COLLECTIONS(tag_bytes.cbegin(),
                                      tag_bytes.cbegin() + 16, tc.tag.cbegin(),
                                      tc.tag.cend());
    }
}

void print_data(const uint8_t *data, const size_t n) {
    printf("[");
    for (size_t i = 0; i < n - 1; ++i)
        printf("%02x, ", data[i]);
    if (n > 0)
        printf("%02x", data[n - 1]);
    printf("]\n");
}

BOOST_DATA_TEST_CASE(RandomPoly1305Tests, bdata::xrange(1000), i) {
    std::mt19937 rng(42 + i); // deterministic per test case
    std::uniform_int_distribution<uint8_t> dist(0, 255);

    // Key
    alignas(64) std::array<uint8_t, 32> key;
    for (auto &x : key)
        x = static_cast<uint8_t>(dist(rng));
    key[3] &= 15;
    key[7] &= 15;
    key[11] &= 15;
    key[15] &= 15;
    key[4] &= 252;
    key[8] &= 252;
    key[12] &= 252;

    // Message
    const size_t message_length = 16 + (dist(rng)) * 16;
    std::vector<uint8_t> message(message_length);
    for (auto &x : message)
        x = static_cast<uint8_t>(dist(rng));

    // Expected tag as per OpenSSL
    alignas(64) std::array<uint8_t, 16> expected_tag;
    EVP_MAC *mac = EVP_MAC_fetch(nullptr, "POLY1305", nullptr);
    EVP_MAC_CTX *ctx = EVP_MAC_CTX_new(mac);
    OSSL_PARAM params[] = {
        // Assuming OpenSSL does not write to the key
        OSSL_PARAM_construct_octet_string(
            "key", const_cast<uint8_t *>(key.data()), key.size()),
        OSSL_PARAM_END};

    EVP_MAC_init(ctx, nullptr, 0, params);
    EVP_MAC_update(ctx, message.data(), message.size());
    size_t tag_len = expected_tag.size();
    EVP_MAC_final(ctx, expected_tag.data(), &tag_len, tag_len);
    EVP_MAC_CTX_free(ctx);
    EVP_MAC_free(mac);
    BOOST_REQUIRE_EQUAL(tag_len, 16);

    // Actual tag, from DSL computation
    std::array<uint8_t, 16> actual_tag;
    poly1305_wrapper(actual_tag.data(), key.data(), message.data(),
                     message.size());
    BOOST_CHECK_EQUAL_COLLECTIONS(actual_tag.cbegin(), actual_tag.cbegin() + 16,
                                  expected_tag.cbegin(), expected_tag.cend());
}
