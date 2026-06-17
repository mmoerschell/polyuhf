#include <array>
#include <cstddef>
#include <cstdint>
#include <random>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include <openssl/evp.h>

#include "generated/datastructures.h"
#include "generated/poly1305.h"

std::array<uint8_t, 16>
openssl_reference_poly1305(const std::array<uint8_t, 32> &key,
                           const std::vector<uint8_t> &message) {
    std::array<uint8_t, 16> tag{};
    size_t out_len = 0;

    EVP_MAC *mac = EVP_MAC_fetch(nullptr, "POLY1305", nullptr);
    BOOST_REQUIRE(mac != nullptr);

    EVP_MAC_CTX *ctx = EVP_MAC_CTX_new(mac);
    BOOST_REQUIRE(ctx != nullptr);

    BOOST_REQUIRE(EVP_MAC_init(ctx, key.data(), key.size(), nullptr) == 1);
    BOOST_REQUIRE(EVP_MAC_update(ctx, message.data(), message.size()) == 1);
    BOOST_REQUIRE(EVP_MAC_final(ctx, tag.data(), &out_len, tag.size()) == 1);
    BOOST_REQUIRE_EQUAL(out_len, tag.size());

    EVP_MAC_CTX_free(ctx);
    EVP_MAC_free(mac);

    return tag;
}

BOOST_DATA_TEST_CASE(RandomPoly1305Tests, boost::unit_test::data::xrange(1000),
                     i) {
    static_assert(FIELD_PI == 130);
    static_assert(FIELD_THETA == 5);
    static_assert(FIELD_CHUNK_SIZE == 16);

    std::mt19937 rng(42 + i); // deterministic per test case
    std::uniform_int_distribution<uint8_t> dist(0, 255);
    std::vector<uint8_t> message(16 * (i + 1)); // message
    std::array<uint8_t, 32> key{};              // key
    for (auto &x : message)
        x = dist(rng);
    // Set s = 0 because it works in a different field and without modular
    // reduction
    for (auto it = key.begin(); it < key.begin() + 16; ++it)
        *it = dist(rng);

    // Clamp key
    key[3] &= 15;
    key[7] &= 15;
    key[11] &= 15;
    key[15] &= 15;
    key[4] &= 252;
    key[8] &= 252;
    key[12] &= 252;

    const auto expected = openssl_reference_poly1305(key, message);
    std::array<uint8_t, FIELD_EXPORT_BYTES> actual{};

    poly1305(actual.data(), key.data(), const_cast<uint8_t *>(message.data()),
             message.size());

    BOOST_CHECK_EQUAL_COLLECTIONS(actual.cbegin(),
                                  actual.cbegin() + expected.size(),
                                  expected.cbegin(), expected.cend());
}
