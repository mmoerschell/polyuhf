#include "addition.h"
#include "configuration.h"

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

#include <cstdint>

using namespace boost::multiprecision;

static const cpp_int c_1305("0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB");

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

BOOST_AUTO_TEST_CASE(SimpleModularReduction) {
    // Constants: 2^130-5, 2^130-6
    const cpp_int c_1306("0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA");

    // Setup:
    // a = 2^130 - 6
    // b = 3000
    // c = a + b (mod 2^130 - 5) = 2999
    alignas(64) bigint_t a{}, b{}, c{};
    export_bits(c_1306, a.limbs, LAMBDA, false);
    b.limbs[0] = 3000;

    // Perform addition
    c = addition(a, b);

    // For reference:
    // cpp_int test = (c_1306 + cpp_int(3000)) % c_1305;
    // export_bits(test, c.limbs, LAMBDA, false);

    // Check value of c
    BOOST_CHECK_EQUAL(c.limbs[0], 2999);
    for (size_t i = 1; i < LIMBS; ++i)
        BOOST_CHECK_EQUAL(c.limbs[i], 0);
}

BOOST_DATA_TEST_CASE(RandomAdditionTests, boost::unit_test::data::xrange(10000),
                     i) {
    std::mt19937 rng(42 + i); // deterministic per test case
    std::uniform_int_distribution<uint32_t> dist(0, LAMBDA_MASK);

    // Create and add two random numbers
    alignas(64) bigint_t a{}, b{}, c{};
    for (size_t i = 0; i < LIMBS; ++i) {
        a.limbs[i] = dist(rng);
        b.limbs[i] = dist(rng);
    }
    c = addition(a, b);

    // Use Boost.MP to verify the solution
    cpp_int ref_a, ref_b, ref_c;
    import_bits(ref_a, a.limbs, a.limbs + LIMBS, LAMBDA, false);
    import_bits(ref_b, b.limbs, b.limbs + LIMBS, LAMBDA, false);
    ref_c = (ref_a + ref_b) % c_1305;
    std::array<uint64_t, LIMBS + 3>
        ref_limbs{}; // who knows how many limbs boost will write
    export_bits(ref_c, ref_limbs.begin(), LAMBDA, false);

    BOOST_CHECK_EQUAL_COLLECTIONS(c.limbs, c.limbs + LIMBS, ref_limbs.cbegin(),
                                  ref_limbs.cbegin() + LIMBS);
}
