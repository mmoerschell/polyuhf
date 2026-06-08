#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>
#include <vector>

#define PI 226ull
#define THETA 5ull
#define CHUNK_SIZE (PI / 8ull)

using namespace boost::multiprecision;

#include "generated/load_store.h"

static const cpp_int prime("0x3fffffffffffffffffffffffffffffffffffffffffffffffffffffffb");

BOOST_AUTO_TEST_CASE(TestLoadStore) {
    std::mt19937 rng(42);
    std::uniform_int_distribution<uint8_t> dist(0, 255);
    const size_t n_blocks = 500;
    std::vector<uint8_t> data(n_blocks * CHUNK_SIZE);
    for (auto &x : data)
        x = dist(rng);
    for (size_t i = 0; i < n_blocks; ++i) {
        auto check = load_store(data.data(), i);
        std::array<uint8_t, CHUNK_SIZE + 1> check_bytes{};
        export_29_bytes(check_bytes.data(), &check);
        BOOST_CHECK_EQUAL_COLLECTIONS(
            check_bytes.cbegin(), check_bytes.cbegin() + CHUNK_SIZE,
            data.begin() + i * CHUNK_SIZE, data.begin() + (i + 1) * CHUNK_SIZE);
        BOOST_CHECK_EQUAL(check_bytes.back(), 0ull);
    }
}

BOOST_AUTO_TEST_CASE(TestSimpleSum) {
    std::mt19937 rng(42);
    std::uniform_int_distribution<uint8_t> dist(0, 255);
    const size_t n_blocks = 500;
    std::vector<uint8_t> data(n_blocks * CHUNK_SIZE);
    cpp_int acc(0);
    for (auto &x : data)
        x = dist(rng);

    for (size_t i = 0; i < n_blocks; ++i) {
        cpp_int data_i(0);
        import_bits(data_i, data.cbegin() + CHUNK_SIZE * i,
                    data.cbegin() + CHUNK_SIZE * (i + 1), 8, false);
        acc = (acc + data_i) % prime;
    }
    auto sum = simple_sum(data.data(), n_blocks);
    std::array<uint8_t, CHUNK_SIZE + 1> expected{}, actual{};
    export_bits(acc, expected.begin(), 8, false);
    export_29_bytes(actual.data(), &sum);
    BOOST_CHECK_EQUAL_COLLECTIONS(actual.cbegin(), actual.cend(),
                                  expected.cbegin(), expected.cend());
}
