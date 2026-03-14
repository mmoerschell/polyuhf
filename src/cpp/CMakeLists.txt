cmake_minimum_required(VERSION 3.20)
project(polyuhf_tests LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

add_executable(tests
    main.cpp
    addition_tests.cpp
    multiplication_tests.cpp
    exponentiation_tests.cpp
    poly1305_tests.cpp
)

target_link_libraries(tests
    PRIVATE
        Boost::json
        Boost::unit_test_framework
        ${OPENSSL_LIBRARIES}
)

target_compile_options(tests PRIVATE
    -Wall
    -Wextra
    -Wpedantic
)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(tests PRIVATE -fsanitize=address,undefined)
    target_link_options(tests PRIVATE -fsanitize=address,undefined)
endif()

target_include_directories(tests PRIVATE . ${OPENSSL_INCLUDE_DIR})
