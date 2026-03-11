#include "poly1305_testcases_loader.hpp"

#include <array>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>
#include <cstdint>
#include <numeric>

#include <openssl/evp.h>

static const std::vector<TestCase> tests =
    load_tests_from_file("src/cpp/poly1305-rfc-test-vectors.json");

namespace bdata = boost::unit_test::data;

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

    BOOST_CHECK_EQUAL_COLLECTIONS(openssl_tag.cbegin(), openssl_tag.cend(),
                                  tc.tag.cbegin(), tc.tag.cend());
}

// BOOST_DATA_TEST_CASE(RandomPoly1305Tests, bdata::xrange(100), i) {
//     std::mt19937 rng(42 + i); // deterministic per test case
//     std::uniform_int_distribution<uint8_t> dist(0, 255);

//     // Key
//     std::array<uint8_t, 32> key;
//     for (auto &x : key)
//         x = static_cast<uint8_t>(dist(rng));
//     key[3] &= 15;
//     key[7] &= 15;
//     key[11] &= 15;
//     key[15] &= 15;
//     key[4] &= 252;
//     key[8] &= 252;
//     key[12] &= 252;

//     // Message
//     const size_t MESSAGE_LENGTH = 256;
//     std::array<uint8_t, MESSAGE_LENGTH> message;
//     for (auto &x : message)
//         x = static_cast<uint8_t>(dist(rng));

//     // Expected tag as per reference
//     std::array<uint8_t, 16> expected_tag;
//     // openssl...(expected_tag.data(), key.data(), message.data(),
//     //              message.size());

//     // Actual tag
//     std::array<uint8_t, 16> actual_tag;
//     poly1305_dsl_wrapper(actual_tag.data(), key.data(), message.data(),
//                          message.size());

//     BOOST_CHECK_EQUAL_COLLECTIONS(actual_tag.cbegin(), actual_tag.cend(),
//                                   expected_tag.cbegin(),
//                                   expected_tag.cend());
// }
