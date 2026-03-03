#include <cstddef>
#include <cstdint>
#include <cstring>
#include <span>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::bit_set;
using boost::multiprecision::cpp_int;
using boost::multiprecision::export_bits;
using boost::multiprecision::import_bits;

void poly1305(uint8_t *tag_, const uint8_t *key_, const uint8_t *message_,
              const size_t M_) {
    const std::span<const uint8_t> r_(key_, 16);
    const std::span<const uint8_t> s_(key_ + 16, 16);
    const std::span<const uint8_t> message(message_, M_);
    const std::span<uint8_t> tag(tag_, 16);
    std::memset(tag.data(), 0, tag.size());

    cpp_int r, s;
    import_bits(r, r_.begin(), r_.end(), 8, false);
    import_bits(s, s_.begin(), s_.end(), 8, false);

    const cpp_int p("0x3fffffffffffffffffffffffffffffffb");
    cpp_int accumulator(0);
    for (auto it = message.begin(); it < message.end(); it += 16) {
        cpp_int block;
        const auto block_size = std::min(message.end() - it, 16L);
        import_bits(block, it, it + block_size, 8, false);
        block = bit_set(block, 8 * block_size);
        accumulator = ((accumulator + block) * r) % p;
    }
    accumulator += s;

    const cpp_int mask("0xffffffffffffffffffffffffffffffff");
    accumulator &= mask;
    export_bits(accumulator, tag.begin(), 8, false);
}
