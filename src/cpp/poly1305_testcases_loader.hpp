#pragma once

#include <array>
#include <cstdint>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include <boost/json.hpp>

namespace json = boost::json;

typedef struct {
    alignas(uint64_t) std::array<uint8_t, 32> key;
    alignas(uint64_t) std::vector<uint8_t> message;
    alignas(uint64_t) std::array<uint8_t, 16> tag;
    std::string description;
} TestCase;

std::ostream& operator<<(std::ostream& os, const TestCase& tc)
{
    return os << "TestCase(" << tc.description << ")";
}

std::string read_file(const std::string &path) {
    std::ifstream f(path);
    if (!f)
        throw std::runtime_error("cannot open file");

    std::stringstream buffer;
    buffer << f.rdbuf();
    return buffer.str();
}

uint8_t hex_val(char c) {
    if ('0' <= c && c <= '9')
        return c - '0';
    if ('a' <= c && c <= 'f')
        return c - 'a' + 10;
    if ('A' <= c && c <= 'F')
        return c - 'A' + 10;
    throw std::runtime_error("invalid hex");
}

std::vector<uint8_t> hex_to_bytes(std::string_view hex) {
    if (hex.size() % 2 != 0)
        throw std::runtime_error("odd hex length");
    std::vector<uint8_t> out(hex.size() / 2);
    for (size_t i = 0; i < out.size(); ++i) {
        out[i] = (hex_val(hex[2 * i]) << 4) | hex_val(hex[2 * i + 1]);
    }
    return out;
}

std::vector<TestCase> load_tests_from_string(const std::string &text) {
    json::value v = json::parse(text);
    auto arr = v.as_array();

    std::vector<TestCase> tests;

    for (auto const &elem : arr) {
        auto const &obj = elem.as_object();

        TestCase t;

        auto key_bytes = hex_to_bytes(obj.at("key").as_string().c_str());
        auto msg_bytes = hex_to_bytes(obj.at("message").as_string().c_str());
        auto tag_bytes = hex_to_bytes(obj.at("tag").as_string().c_str());

        std::copy(key_bytes.begin(), key_bytes.end(), t.key.begin());
        t.message = std::move(msg_bytes);
        std::copy(tag_bytes.begin(), tag_bytes.end(), t.tag.begin());
        t.description = obj.at("description").as_string().c_str();

        tests.push_back(std::move(t));
    }

    return tests;
}

std::vector<TestCase> load_tests_from_file(const std::string &path) {
    const auto text = read_file(path);
    return load_tests_from_string(text);
}
