#include <array>
#include <cstddef>
#include <cstdint>
#include <random>
#include <vector>

#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include "datastructures.h"
#include "hkm.h"
#include "hkm_iter.h"

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
    hkm(recursive.data(), key.data(), message.data(), byte_len);
    hkm_iter(iterative.data(), key.data(), message.data(), byte_len);

    BOOST_CHECK_EQUAL_COLLECTIONS(iterative.cbegin(), iterative.cend(),
                                  recursive.cbegin(), recursive.cend());
}
