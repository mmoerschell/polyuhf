#pragma once

#include <boost/multiprecision/cpp_int.hpp>
#include <string>

std::string to_little_endian_hex(const boost::multiprecision::cpp_int &x);
