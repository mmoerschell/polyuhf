#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::multiprecision;
namespace bdata = boost::unit_test::data;

#include "generated/mmh.h"
#include "generated/nmh.h"
#include "generated/sqh.h"

static const cpp_int c1163("0xffffffffffffffffffffffffffffd");

BOOST_DATA_TEST_CASE(Random_MMH_SQH_Tests, bdata::xrange(100), i) {
    std::mt19937 rng(42 + i); // deterministic per test case
    std::uniform_int_distribution<uint8_t> dist(0, 255);

    // FIXME TODO
    const size_t B = 4 * i + 1;     // number of blocks
    std::vector<uint8_t> M(B * 14); // message
    std::vector<uint8_t> r(B * 14); // key
    for (auto &x : M)
        x = dist(rng);
    for (auto &x : r)
        x = dist(rng);

    // Reference computations
    cpp_int mmh_acc(0), sqh_acc(0);
    for (size_t i = 0; i < B - 1; ++i) {
        cpp_int Mi{}, ri{};
        import_bits(Mi, M.cbegin() + 14 * i, M.cbegin() + 14 * (i + 1), 8,
                    false);
        import_bits(ri, r.cbegin() + 14 * i, r.cbegin() + 14 * (i + 1), 8,
                    false);
        mmh_acc = (mmh_acc + Mi * ri) % c1163;
        sqh_acc = (sqh_acc + (Mi + ri) * (Mi + ri)) % c1163;
    }
    cpp_int MB{};
    import_bits(MB, M.cend() - 14, M.cend(), 8, false);
    mmh_acc = (mmh_acc + MB) % c1163;
    sqh_acc = (sqh_acc + MB) % c1163;
    std::array<uint8_t, 15> mmh_tag_ref{};
    std::array<uint8_t, 15> sqh_tag_ref{};
    export_bits(mmh_acc, mmh_tag_ref.begin(), 8, false);
    export_bits(sqh_acc, sqh_tag_ref.begin(), 8, false);
    
    // DSL computation
    auto mmh_bigint = mmh(M.data(), r.data(), B);
    auto sqh_bigint = sqh(M.data(), r.data(), B);
    std::array<uint8_t, 15> mmh_tag_act{}, sqh_tag_act{};
    export_15_bytes(mmh_tag_act.data(), &mmh_bigint);
    export_15_bytes(sqh_tag_act.data(), &sqh_bigint);

    // Compare
    BOOST_CHECK_EQUAL_COLLECTIONS(mmh_tag_act.cbegin(), mmh_tag_act.cend(),
                                  mmh_tag_ref.cbegin(), mmh_tag_ref.cend());
    BOOST_CHECK_EQUAL_COLLECTIONS(sqh_tag_act.cbegin(), sqh_tag_act.cend(),
                                  sqh_tag_ref.cbegin(), sqh_tag_ref.cend());
}

BOOST_DATA_TEST_CASE(Random_NMH_Tests, bdata::xrange(100), i) {
    std::mt19937 rng(42 + i); // deterministic per test case
    std::uniform_int_distribution<uint8_t> dist(0, 255);

    const size_t B = 4 * i;        // number of blocks
    std::vector<uint8_t> M(B * 14); // message
    std::vector<uint8_t> r(B * 14); // key
    for (auto &x : M)
        x = dist(rng);
    for (auto &x : r)
        x = dist(rng);

    // Reference computation
    cpp_int acc(0);
    for (size_t i = 0; i < B / 2; ++i) {
        cpp_int M2i{}, r2i{}, M2i1{}, r2i1{};
        import_bits(M2i, M.cbegin() + 14 * (2 * i),
                    M.cbegin() + 14 * (2 * i + 1), 8, false);
        import_bits(r2i, r.cbegin() + 14 * (2 * i),
                    r.cbegin() + 14 * (2 * i + 1), 8, false);
        import_bits(M2i1, M.cbegin() + 14 * (2 * i + 1),
                    M.cbegin() + 14 * (2 * i + 2), 8, false);
        import_bits(r2i1, r.cbegin() + 14 * (2 * i + 1),
                    r.cbegin() + 14 * (2 * i + 2), 8, false);
        acc += (M2i + r2i) * (M2i1 + r2i1);
        acc %= c1163;
    }
    std::array<uint8_t, 15> tag_ref{};
    export_bits(acc, tag_ref.begin(), 8, false);

    // DSL output
    std::array<uint8_t, 15> tag_act{};
    auto result = nmh( M.data(), r.data(), B);
    export_15_bytes(tag_act.data(), &result);

    // Compare
    BOOST_CHECK_EQUAL_COLLECTIONS(tag_act.cbegin(), tag_act.cend(),
                                  tag_ref.cbegin(), tag_ref.cend());
}
