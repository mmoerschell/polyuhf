#include "little_endian_hex.h"

std::string to_little_endian_hex(const boost::multiprecision::cpp_int &x) {
    std::vector<unsigned char> bytes;

    // Export in little-endian byte order
    export_bits(x, std::back_inserter(bytes), 8, false);

    // Handle zero specially
    if (bytes.empty())
        bytes.push_back(0);

    std::ostringstream oss;

    for (unsigned char b : bytes) {
        oss << std::hex << std::setw(2) << std::setfill('0')
            << static_cast<int>(b);
    }

    return oss.str();
}
