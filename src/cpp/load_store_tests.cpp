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
        std::array<uint8_t, 15> check{};
        load_store(check.data(), data.data(), i);
        BOOST_CHECK_EQUAL_COLLECTIONS(check.cbegin(), check.cbegin() + block_size,
                                      data.begin() + i * block_size,
                                      data.begin() + (i + 1) * block_size);
                                      BOOST_CHECK_EQUAL(check.back(), 0ull);
    }
}
