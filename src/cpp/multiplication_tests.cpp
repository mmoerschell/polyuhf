#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include "field_config.h"
#include "squareto1.h"

using namespace boost::multiprecision;

static const cpp_int prime(FIELD_PRIME_HEX);
static const cpp_int squareto1_input("0xffffffffffffffffffffffffffffc");

BOOST_AUTO_TEST_CASE(MultiplicationMaxTest) {
    cpp_int ref = (squareto1_input * squareto1_input) % prime;
    auto act = squareto1();
    std::array<uint8_t, FIELD_EXPORT_BYTES> ref_bytes{}, act_bytes{};
    export_bits(ref, ref_bytes.begin(), 8, false);
    export_field_bytes(act_bytes.data(), &act);

    BOOST_CHECK_EQUAL_COLLECTIONS(ref_bytes.cbegin(), ref_bytes.cend(),
                                  act_bytes.cbegin(), act_bytes.cend());
}
