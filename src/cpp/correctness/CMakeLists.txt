cmake_minimum_required(VERSION 3.20)
project(polyuhf_correctness LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(GENERATED_DIR "" CACHE PATH "Generated PolyUHF source directory")
if(NOT GENERATED_DIR)
    message(FATAL_ERROR "Set GENERATED_DIR to the generated source directory")
endif()
get_filename_component(GENERATED_DIR "${GENERATED_DIR}" ABSOLUTE)
if(NOT EXISTS "${GENERATED_DIR}")
    message(FATAL_ERROR "GENERATED_DIR does not exist: ${GENERATED_DIR}")
endif()
if(NOT EXISTS "${GENERATED_DIR}/datastructures.h")
    message(FATAL_ERROR "GENERATED_DIR does not contain datastructures.h: ${GENERATED_DIR}")
endif()
get_filename_component(GENERATED_PARENT_DIR "${GENERATED_DIR}/.." ABSOLUTE)

file(READ "${GENERATED_DIR}/datastructures.h" GENERATED_DATASTRUCTURES_H)
if(GENERATED_DATASTRUCTURES_H MATCHES "immintrin\\.h")
    set(POLYUHF_NEEDS_AVX2 TRUE)
else()
    set(POLYUHF_NEEDS_AVX2 FALSE)
endif()

find_package(Boost CONFIG REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

file(GLOB_RECURSE GENERATED_SOURCES CONFIGURE_DEPENDS "${GENERATED_DIR}/*.c")
file(GLOB_RECURSE GENERATED_PERF_SOURCES CONFIGURE_DEPENDS "${GENERATED_DIR}/*_perf.c")
list(REMOVE_ITEM GENERATED_SOURCES ${GENERATED_PERF_SOURCES})
file(GLOB_RECURSE GENERATED_AUTOTESTS CONFIGURE_DEPENDS "${GENERATED_DIR}/*autotests.cpp")

set(POLYUHF_CPP_DIR "${CMAKE_CURRENT_LIST_DIR}/..")
set(MANUAL_TEST_SOURCES)
if(EXISTS "${GENERATED_DIR}/load_store.h")
    list(APPEND MANUAL_TEST_SOURCES "${POLYUHF_CPP_DIR}/load_store_tests.cpp")
endif()
if(EXISTS "${GENERATED_DIR}/squareto1.h")
    list(APPEND MANUAL_TEST_SOURCES "${POLYUHF_CPP_DIR}/multiplication_tests.cpp")
endif()

add_executable(correctness
    "${POLYUHF_CPP_DIR}/main.cpp"
    "${POLYUHF_CPP_DIR}/little_endian_hex.cpp"
    ${MANUAL_TEST_SOURCES}
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

if(POLYUHF_NEEDS_AVX2)
    target_compile_options(correctness PRIVATE -mavx2)
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(correctness PRIVATE -fsanitize=address,undefined)
    target_link_options(correctness PRIVATE -fsanitize=address,undefined)
endif()

target_include_directories(correctness PRIVATE
    ${GENERATED_DIR}
    ${GENERATED_PARENT_DIR}
    ${POLYUHF_CPP_DIR}
    ${OPENSSL_INCLUDE_DIR}
)
