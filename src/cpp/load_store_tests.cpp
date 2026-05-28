#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>
#include <vector>

using namespace boost::multiprecision;

#include "generated/load_store.h"

static const cpp_int c1163("0xffffffffffffffffffffffffffffd");

BOOST_AUTO_TEST_CASE(TestLoadStore) {
    std::mt19937 rng(42);
    std::uniform_int_distribution<uint8_t> dist(0, 255);
    const size_t n_blocks = 500;
    const size_t block_size = 14;
    std::vector<uint8_t> data(n_blocks * block_size);
    for (auto &x : data)
        x = dist(rng);
    for (size_t i = 0; i < n_blocks; ++i) {
        auto check = load_store(data.data(), i);
        std::array<uint8_t, 15> check_bytes{};
        export_15_bytes(check_bytes.data(), &check);
        BOOST_CHECK_EQUAL_COLLECTIONS(
            check_bytes.cbegin(), check_bytes.cbegin() + block_size,
            data.begin() + i * block_size, data.begin() + (i + 1) * block_size);
        BOOST_CHECK_EQUAL(check_bytes.back(), 0ull);
    }
}

BOOST_AUTO_TEST_CASE(TestSimpleSum) {
    std::mt19937 rng(42);
    std::uniform_int_distribution<uint8_t> dist(0, 255);
    const size_t n_blocks = 500;
    const size_t block_size = 14;
    std::vector<uint8_t> data(n_blocks * block_size);
    cpp_int acc(0);
    for (auto &x : data)
        x = dist(rng);

    for (size_t i = 0; i < n_blocks; ++i) {
        cpp_int data_i(0);
        import_bits(data_i, data.cbegin() + 14 * i,
                    data.cbegin() + 14 * (i + 1), 8, false);
        acc = (acc + data_i) % c1163;
    }
    auto sum = simple_sum(data.data(), n_blocks);
    std::array<uint8_t, 15> expected{}, actual{};
    export_bits(acc, expected.begin(), 8, false);
    export_15_bytes(actual.data(), &sum);
    BOOST_CHECK_EQUAL_COLLECTIONS(actual.cbegin(), actual.cend(),
                                  expected.cbegin(), expected.cend());
}
