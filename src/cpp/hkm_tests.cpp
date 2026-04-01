#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>
#include <random>
#include <vector>

using namespace boost::multiprecision;
namespace bdata = boost::unit_test::data;

#include "generated/hkm.h"

static const cpp_int c_1305("0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB");

bigint_t random_bigint(std::mt19937 &rng) {
    bigint_t x{};
    std::uniform_int_distribution<uint64_t> dist(0, LAMBDA_MASK);
    for (auto &l : x.limbs)
        l = dist(rng);
    x.limbs[LIMBS - 1] &= LAMBDA_PRIME_MASK;
    return x;
}

cpp_int hkm_ref(const std::vector<cpp_int> &r, const std::vector<cpp_int> &M,
                const size_t B) {
    if (B == 1) {
        return (r[0] + M[0]) % c_1305;
    } else {
        cpp_int res =
            hkm_ref(r, r, 2 * (B / 2) - 1) * (r[B / 2] + M[2 * (B / 2) - 1]);
        if (B % 2)
            res += M[B - 1];
        return res % c_1305;
    }
}

BOOST_AUTO_TEST_CASE(HKMBaseCase) {
    std::mt19937 rng(42);
    bigint_t r = random_bigint(rng), M = random_bigint(rng);
    const auto res = hkm(&r, &M, 1);
    std::array<uint8_t, 17> tag_ref, tag_act;
    to_le_bytes(tag_act.data(), tag_act.size(), &res);
    cpp_int r_ref, M_ref, res_ref;
    import_bits(r_ref, r.limbs, r.limbs + LIMBS, LAMBDA, false);
    import_bits(M_ref, M.limbs, M.limbs + LIMBS, LAMBDA, false);
    res_ref = (r_ref + M_ref) % c_1305;
    export_bits(res_ref, tag_ref.data(), 8, false);
    BOOST_CHECK_EQUAL_COLLECTIONS(tag_act.cbegin(), tag_act.cend(),
                                  tag_ref.cbegin(), tag_ref.cend());
}

BOOST_DATA_TEST_CASE(RandomHKMTests, bdata::xrange(1000), i) {
    const size_t len = i / 5 + 1; // 5 testcases per message length
    BOOST_REQUIRE_GE(len, 1);

    // Get random r, M
    std::mt19937 rng(42 + i);
    std::vector<bigint_t> r(len), M(len);
    std::vector<cpp_int> r_ref(len), M_ref(len);
    for (size_t i = 0; i < len; ++i) {
        r[i] = random_bigint(rng);
        M[i] = random_bigint(rng);
        import_bits(r_ref[i], r[i].limbs, r[i].limbs + LIMBS, LAMBDA, false);
        import_bits(M_ref[i], M[i].limbs, M[i].limbs + LIMBS, LAMBDA, false);
    }

    // Computation
    std::array<uint8_t, 17> tag_act{}, tag_ref{};

    const auto res = hkm(r.data(), M.data(), len);
    to_le_bytes(tag_act.data(), tag_act.size(), &res);

    const auto res_ref = hkm_ref(r_ref, M_ref, len);
    export_bits(res_ref, tag_ref.begin(), 8, false);

    // Compare
    BOOST_CHECK_EQUAL_COLLECTIONS(tag_act.cbegin(), tag_act.cend(),
                                  tag_ref.cbegin(), tag_ref.cend());
}
