#include <algorithm>
#include <array>
#include <cstddef>
#include <cstdint>
#include <random>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include "generated/datastructures.h"
#include "generated/hkm_iter.h"

const boost::multiprecision::cpp_int prime(FIELD_PRIME_HEX);

boost::multiprecision::cpp_int load(const uint8_t *buffer,
                                    const size_t position) {
    boost::multiprecision::cpp_int res(0);
    boost::multiprecision::import_bits(
        res, &buffer[FIELD_CHUNK_SIZE * position],
        &buffer[FIELD_CHUNK_SIZE * (position + 1)], 8, false);
    return res;
};

boost::multiprecision::cpp_int
hkm_recursive(const uint8_t *key, const uint8_t *message, const size_t B) {
    if (B == 1) {
        return (load(message, 0) + load(key, 0)) % prime;
    } else {
        const size_t half = B / 2;
        const size_t even_message_index = 2 * half - 1;
        auto acc = hkm_recursive(key, message, even_message_index);
        acc *= load(key, half) + load(message, even_message_index);
        if (B & 1) {
            acc += load(message, B - 1);
        }
        return acc % prime;
    }
}

void hkm_recursive_wrapper(uint8_t *output, uint8_t *key, uint8_t *message,
                 size_t buffer_length) {
    const size_t B = (buffer_length + FIELD_CHUNK_SIZE - 1) / FIELD_CHUNK_SIZE;
    const auto value = hkm_recursive(key, message, B) % prime;
    std::fill_n(output, FIELD_EXPORT_BYTES, 0);
    export_bits(value, output, 8, false);
}

BOOST_DATA_TEST_CASE(HKMIterativeMatchesRecursive,
                     boost::unit_test::data::xrange(256), i) {
    std::mt19937 rng(42 + i);
    std::uniform_int_distribution<uint8_t> dist(0, 255);

    const size_t blocks = i + 1;
    const size_t byte_len = blocks * FIELD_CHUNK_SIZE;
    std::vector<uint8_t> key(byte_len + 100);
    std::vector<uint8_t> message(byte_len + 100);
    for (auto &x : key)
        x = dist(rng);
    for (auto &x : message)
        x = dist(rng);

    std::array<uint8_t, FIELD_EXPORT_BYTES> recursive{}, iterative{};
    hkm_recursive_wrapper(recursive.data(), key.data(), message.data(), byte_len);
    hkm_iter(iterative.data(), key.data(), message.data(), byte_len);

    BOOST_CHECK_EQUAL_COLLECTIONS(iterative.cbegin(), iterative.cend(),
                                  recursive.cbegin(), recursive.cend());
}
