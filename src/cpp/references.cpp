#include <print>
#include <stdexcept>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;

cpp_int mmh(const std::vector<cpp_int> &M, const std::vector<cpp_int> &r) {
    // TODO modular reductions over prime field
    if (M.size() != r.size() + 1)
        throw std::runtime_error(
            "Message should have one more element than the key");
    cpp_int result(0);
    for (size_t i = 0; i < r.size(); ++i)
        result += M[i] + r[i];
    result += M.back();
    return result;
}

cpp_int nmh(const std::vector<cpp_int> &M, const std::vector<cpp_int> &r) {
    // TODO modular reductions over prime field
    if (M.size() != r.size() || M.empty())
        throw std::runtime_error(
            "Message and key must be of identical non-zero length");
    cpp_int result(0);
    for (size_t i = 0; i < M.size() / 2; ++i)
        result += (M[2 * i] + r[2 * i]) * (M[2 * i + 1] + r[2 * i + 1]);
    return result;
}
