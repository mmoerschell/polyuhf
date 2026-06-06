cmake_minimum_required(VERSION 3.20)
project(polyuhf_tests LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost CONFIG REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

# Automatically grab all generated function files and autotest source files
file(GLOB_RECURSE GENERATED_SOURCES CONFIGURE_DEPENDS "generated/*.c")
file(GLOB_RECURSE GENERATED_PERF_SOURCES CONFIGURE_DEPENDS "generated/*_perf.c")
list(REMOVE_ITEM GENERATED_SOURCES ${GENERATED_PERF_SOURCES})
file(GLOB_RECURSE GENERATED_AUTOTESTS CONFIGURE_DEPENDS "generated/*autotests.cpp")

add_executable(correctness
    main.cpp
    little_endian_hex.cpp
    load_store_tests.cpp
    multiplication_tests.cpp
    hashing_tests.cpp
    # poly1305_tests.cpp
    ${GENERATED_SOURCES}
    ${GENERATED_AUTOTESTS}
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
    -Wno-unused-variable
)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(correctness PRIVATE -fsanitize=address,undefined)
    target_link_options(correctness PRIVATE -fsanitize=address,undefined)
endif()

target_include_directories(correctness PRIVATE . ${OPENSSL_INCLUDE_DIR})
