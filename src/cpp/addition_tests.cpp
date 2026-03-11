#include "configuration.h"
#include "addition.h"

#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include <cstdint>

using namespace boost::multiprecision;

BOOST_AUTO_TEST_CASE(SimpleAddition1) {
    bigint_t a{}, b{}, c{};
    a.limbs[0] = 42;
    b.limbs[0] = 1;
    c = addition(a, b);
    BOOST_CHECK_EQUAL(c.limbs[0], 43);
    for (size_t i = 1; i < LIMBS; ++i)
        BOOST_CHECK_EQUAL(c.limbs[i], 0);
}

BOOST_AUTO_TEST_CASE(SimpleCarry1) {
    bigint_t a{}, b{}, c{};
    a.limbs[0] = LAMBDA_MASK;
    b.limbs[0] = 1;
    c = addition(a, b);
    BOOST_CHECK_EQUAL(c.limbs[0], 0);
    BOOST_CHECK_EQUAL(c.limbs[1], 1);
    for (size_t i = 2; i < LIMBS; ++i)
        BOOST_CHECK_EQUAL(c.limbs[i], 0);
}

BOOST_AUTO_TEST_CASE(SimpleCarry2) {
    bigint_t a{}, b{}, c{};
    a.limbs[0] = LAMBDA_MASK;
    b.limbs[0] = LAMBDA_MASK;
    c = addition(a, b);
    BOOST_CHECK_EQUAL(c.limbs[0], LAMBDA_MASK - 1);
    BOOST_CHECK_EQUAL(c.limbs[1], 1);
    for (size_t i = 2; i < LIMBS; ++i)
        BOOST_CHECK_EQUAL(c.limbs[i], 0);
}

// BOOST_DATA_TEST_CASE(RandomAdditionTests, boost::unit_test::data::xrange(100),
//                      i) {
//     std::mt19937 rng(42 + i); // deterministic per test case
//     std::uniform_int_distribution<uint32_t> dist(0, LAMBDA_MASK);

//     // Create and add two random numbers
//     alignas(64) bigint_t a, b, c;
//     for (size_t i = 0; i < LIMBS; ++i) {
//         a.limbs[i] = dist(rng);
//         b.limbs[i] = dist(rng);
//     }
//     c = addition(a, b);

//     // Use Boost.MP to verify the solution
//     cpp_int ref_a, ref_b, ref_c;
//     import_bits(ref_a, a.limbs, a.limbs + LIMBS, 22, false);
//     import_bits(ref_b, b.limbs, b.limbs + LIMBS, 22, false);
//     ref_c = ref_a + ref_b;
//     std::array<uint64_t, LIMBS> ref_limbs;
//     export_bits(ref_c, ref_limbs.begin(), 22, false);

//     BOOST_CHECK_EQUAL_COLLECTIONS(c.limbs, c.limbs + LIMBS, ref_limbs.cbegin(), ref_limbs.cend());
// }
