#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>
#include <boost/range/irange.hpp>
#include <print>

#include "generated/datastructures.h"
#include "little_endian_hex.h"
#include "generated/squareto1.h"

using namespace boost::multiprecision;

static const cpp_int c1163("0xffffffffffffffffffffffffffffd");
static const cpp_int max_field(c1163 - 1);

// BOOST_DATA_TEST_CASE(MultiplicationMaxTests, boost::irange<size_t>(5), i) {
BOOST_AUTO_TEST_CASE(MultiplicationMaxTest) {
    // Reference computation
    size_t i = 2;
    // std::println("i = {}", i);
    cpp_int ref(1);
    for (size_t j = 0; j <i; ++j)
        ref = (ref * max_field) % c1163;
    // std::println("{}", to_little_endian_hex(ref));


    auto act = squareto1();
    std::array<uint8_t, 15> ref_bytes{}, act_bytes{};
    export_bits(ref, ref_bytes.begin(), 8, false);
    export_15_bytes(act_bytes.data(), &act);

    // BOOST_CHECK_EQUAL_COLLECTIONS(ref_bytes.cbegin(), ref_bytes.cend(), act_bytes.cbegin(), act_bytes.cend());

}
