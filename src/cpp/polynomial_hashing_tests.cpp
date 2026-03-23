#include <array>
#include <cstddef>
#include <cstdint>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/test/data/monomorphic.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::multiprecision;
namespace bdata = boost::unit_test::data;

#include "util.hpp"

#include "generated/configuration.h"
#include "generated/mmh.h"
#include "generated/nmh.h"
#include "generated/sqh.h"

static const cpp_int c_1305("0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB");

BOOST_DATA_TEST_CASE(RandomPolyHashingTests, bdata::xrange(1000), i) {
    std::mt19937 rng(42 + i); // deterministic per test case
    std::uniform_int_distribution<uint8_t> dist(0, 255);

    const size_t B = i + 1;         // number of blocks
    std::vector<uint8_t> M(B * 16); // message
    std::vector<uint8_t> r(B * 16); // key
    for (auto &x : M)
        x = dist(rng);
    for (auto &x : r)
        x = dist(rng);

    // MMH
    {
        cpp_int acc(0);
        for (size_t i = 0; i < B - 1; ++i) {
            cpp_int Mi{}, ri{};
            import_bits(Mi, M.cbegin() + 16 * i, M.cbegin() + 16 * (i + 1), 8,
                        false);
            import_bits(ri, r.cbegin() + 16 * i, r.cbegin() + 16 * (i + 1), 8,
                        false);
            acc += Mi * ri;
            acc %= c_1305;
        }
        cpp_int MB{};
        import_bits(MB, M.cend() - 16, M.cend(), 8, false);
        acc = (acc + MB) % c_1305;
        std::array<uint8_t, 17> tag_ref{};
        export_bits(acc, tag_ref.begin(), 8, false);

        std::vector<bigint_t> M_bi(B, bigint_t{}), r_bi(B, bigint_t{});
        for (size_t i = 0; i < B; ++i) {
            M_bi[i] = from_le_bytes(M.data() + 16 * i, 16);
            r_bi[i] = from_le_bytes(r.data() + 16 * i, 16);
        }
        auto dsl_out = mmh(r_bi.data(), M_bi.data(), B);
        std::array<uint8_t, 17> tag_act{};
        to_le_bytes(tag_act.data(), 17, dsl_out);
        BOOST_CHECK_EQUAL_COLLECTIONS(tag_act.cbegin(), tag_act.cend(),
                                      tag_ref.cbegin(), tag_ref.cend());
    }

    // SQH
    {
        cpp_int acc(0);
        for (size_t i = 0; i < B - 1; ++i) {
            cpp_int Mi{}, ri{};
            import_bits(Mi, M.cbegin() + 16 * i, M.cbegin() + 16 * (i + 1), 8,
                        false);
            import_bits(ri, r.cbegin() + 16 * i, r.cbegin() + 16 * (i + 1), 8,
                        false);
            acc += (Mi + ri) * (Mi + ri);
            acc %= c_1305;
        }
        cpp_int MB{};
        import_bits(MB, M.cend() - 16, M.cend(), 8, false);
        acc = (acc + MB) % c_1305;
        std::array<uint8_t, 17> tag_ref{};
        export_bits(acc, tag_ref.begin(), 8, false);

        std::vector<bigint_t> M_bi(B, bigint_t{}), r_bi(B, bigint_t{});
        for (size_t i = 0; i < B; ++i) {
            M_bi[i] = from_le_bytes(M.data() + 16 * i, 16);
            r_bi[i] = from_le_bytes(r.data() + 16 * i, 16);
        }
        auto dsl_out = sqh(r_bi.data(), M_bi.data(), B);
        std::array<uint8_t, 17> tag_act{};
        to_le_bytes(tag_act.data(), 17, dsl_out);
        BOOST_CHECK_EQUAL_COLLECTIONS(tag_act.cbegin(), tag_act.cend(),
                                      tag_ref.cbegin(), tag_ref.cend());
    }

    // NMH
    // Assuming even message length
    if (B % 2 == 0) {
        cpp_int acc(0);
        for (size_t i = 0; i < B / 2; ++i) {
            cpp_int M2i{}, r2i{}, M2i1{}, r2i1{};
            import_bits(M2i, M.cbegin() + 16 * (2 * i),
                        M.cbegin() + 16 * (2 * i + 1), 8, false);
            import_bits(M2i1, M.cbegin() + 16 * (2 * i + 1),
                        M.cbegin() + 16 * (2 * i + 2), 8, false);
            import_bits(r2i, r.cbegin() + 16 * (2 * i),
                        r.cbegin() + 16 * (2 * i + 1), 8, false);
            import_bits(r2i1, r.cbegin() + 16 * (2 * i + 1),
                        r.cbegin() + 16 * (2 * i + 2), 8, false);
            acc += (M2i + r2i) * (M2i1 + r2i1);
            acc %= c_1305;
        }
        std::array<uint8_t, 17> tag_ref{};
        export_bits(acc, tag_ref.begin(), 8, false);

        std::vector<bigint_t> M_bi(B, bigint_t{}), r_bi(B, bigint_t{});
        for (size_t i = 0; i < B; ++i) {
            M_bi[i] = from_le_bytes(M.data() + 16 * i, 16);
            r_bi[i] = from_le_bytes(r.data() + 16 * i, 16);
        }
        auto dsl_out = nmh(r_bi.data(), M_bi.data(), B);
        std::array<uint8_t, 17> tag_act{};
        to_le_bytes(tag_act.data(), 17, dsl_out);
        BOOST_CHECK_EQUAL_COLLECTIONS(tag_act.cbegin(), tag_act.cend(),
                                      tag_ref.cbegin(), tag_ref.cend());
    }

    // HKM
    // TODO: DSL function calls, recursion
}
