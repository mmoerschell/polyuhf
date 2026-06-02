cmake_minimum_required(VERSION 3.20)
project(polyuhf_tests LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost CONFIG REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

add_executable(correctness
    main.cpp
    little_endian_hex.cpp
    load_store_tests.cpp
    multiplication_tests.cpp
    hashing_tests.cpp
    # poly1305_tests.cpp
    generated/datastructures.c
    generated/load_store.c
    generated/squareto1.c
    generated/mmh.c
    generated/sqh.c
    generated/nmh.c
)

target_link_libraries(correctness
    PRIVATE
        Boost::json
        Boost::unit_test_framework
        ${OPENSSL_LIBRARIES}
)

target_compile_options(correctness PRIVATE
    -Wall
    -Wextra
    -Wpedantic
)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(correctness PRIVATE -fsanitize=address,undefined)
    target_link_options(correctness PRIVATE -fsanitize=address,undefined)
endif()

target_include_directories(correctness PRIVATE . ${OPENSSL_INCLUDE_DIR})

add_executable(performance
    performance.c
    generated/nmh.c
)

target_compile_options(performance PRIVATE
    -Wall
    -Wextra
    -Wpedantic
    -O3
    -mcpu=native
    -march=armv8.2-a+simd+dotprod
    -DNDEBUG
    -fno-vectorize
    -fno-slp-vectorize
)
