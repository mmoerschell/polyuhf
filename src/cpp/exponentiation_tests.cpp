#include "configuration.h"
#include "exponentiation.h"

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include <cstdint>

using namespace boost::multiprecision;

static const cpp_int c_1305("0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB");

BOOST_AUTO_TEST_CASE(SimpleSquare) {
    bigint_t a{}, b{};
    a.limbs[0] = 42;
    b = exponentiation(a, 2);
    BOOST_CHECK_EQUAL(b.limbs[0], 1764);
    for (size_t i = 1; i < LIMBS; ++i)
        BOOST_CHECK_EQUAL(b.limbs[i], 0);
}

BOOST_AUTO_TEST_CASE(SimpleExponentiation) {
    bigint_t a{}, b{};
    a.limbs[0] = 12345;
    b = exponentiation(a, 6);

    alignas(64) std::array<uint64_t, LIMBS + 3> ref_limbs{};
    cpp_int solution("3539537889086624823140625");
    export_bits(solution, ref_limbs.begin(), LAMBDA, false);
    BOOST_CHECK_EQUAL_COLLECTIONS(b.limbs, b.limbs + LIMBS, ref_limbs.cbegin(), ref_limbs.cbegin() + LIMBS);
}

// BOOST_DATA_TEST_CASE(RandomExpTests, boost::unit_test::data::xrange(100), i) {
//     std::mt19937 rng(42 + i); // deterministic per test case
//     std::uniform_int_distribution<uint32_t> dist_limb_bits(0, LAMBDA_MASK);
//     std::uniform_int_distribution<uint32_t> dist_exponent(0, 10);

//     // Create a random number, raise it to a random power
//     const auto exponent = dist_exponent(rng);
//     alignas(64) bigint_t a{}, b;
//     for (size_t i = 0; i < LIMBS; ++i)
//         a.limbs[i] = dist_limb_bits(rng);
//     b = exponentiation(a, exponent);

//     // Use Boost.MP to verify the solution
//     cpp_int ref_a, ref_b;
//     import_bits(ref_a, a.limbs, a.limbs + LIMBS, LAMBDA, false);
//     ref_b = (ref_a ^ exponent) % c_1305;
//     std::array<uint64_t, LIMBS + 3>
//         ref_limbs{}; // who knows how many limbs boost will write
//     export_bits(ref_b, ref_limbs.begin(), LAMBDA, false);

//     BOOST_CHECK_EQUAL_COLLECTIONS(b.limbs, b.limbs + LIMBS, ref_limbs.cbegin(),
//                                   ref_limbs.cbegin() + LIMBS);
// }
