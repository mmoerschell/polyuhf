cmake_minimum_required(VERSION 3.20)
project(polyuhf_tests LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost CONFIG REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

set(GENERATED_DIR "" CACHE PATH "Generated PolyUHF source directory")
if(NOT GENERATED_DIR)
    message(FATAL_ERROR "Set GENERATED_DIR to the runner-generated source directory")
endif()
get_filename_component(GENERATED_DIR "${GENERATED_DIR}" ABSOLUTE)
if(NOT EXISTS "${GENERATED_DIR}")
    message(FATAL_ERROR "GENERATED_DIR does not exist: ${GENERATED_DIR}")
endif()
get_filename_component(GENERATED_PARENT_DIR "${GENERATED_DIR}/.." ABSOLUTE)

# Automatically grab all generated function files and autotest source files
file(GLOB_RECURSE GENERATED_SOURCES CONFIGURE_DEPENDS "${GENERATED_DIR}/*.c")
file(GLOB_RECURSE GENERATED_PERF_SOURCES CONFIGURE_DEPENDS "${GENERATED_DIR}/*_perf.c")
list(REMOVE_ITEM GENERATED_SOURCES ${GENERATED_PERF_SOURCES})
file(GLOB_RECURSE GENERATED_AUTOTESTS CONFIGURE_DEPENDS "${GENERATED_DIR}/*autotests.cpp")

add_executable(correctness
    main.cpp
    little_endian_hex.cpp
    load_store_tests.cpp
    multiplication_tests.cpp
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

file(READ "${GENERATED_DIR}/datastructures.h" GENERATED_DATASTRUCTURES_H)
if(GENERATED_DATASTRUCTURES_H MATCHES "immintrin\\.h")
    target_compile_options(correctness PRIVATE -mavx2)
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(correctness PRIVATE -fsanitize=address,undefined)
    target_link_options(correctness PRIVATE -fsanitize=address,undefined)
endif()

target_include_directories(correctness PRIVATE
    ${GENERATED_DIR}
    ${GENERATED_PARENT_DIR}
    .
    ${OPENSSL_INCLUDE_DIR}
)

foreach(PERF_SOURCE ${GENERATED_PERF_SOURCES})
    get_filename_component(PERF_STEM "${PERF_SOURCE}" NAME_WE)
    string(REGEX REPLACE "_perf$" "" PERF_MODULE "${PERF_STEM}")
    set(PERF_LIBRARY "${GENERATED_DIR}/${PERF_MODULE}.c")
    if(EXISTS "${PERF_LIBRARY}")
        add_executable("${PERF_STEM}"
            "${PERF_LIBRARY}"
            "${PERF_SOURCE}"
            "${GENERATED_DIR}/datastructures.c"
        )
        target_include_directories("${PERF_STEM}" PRIVATE
            ${GENERATED_DIR}
            ${GENERATED_PARENT_DIR}
            .
        )
        target_compile_options("${PERF_STEM}" PRIVATE
            -Wall
            -Wextra
            -Wpedantic
            -Wno-format-zero-length
        )
        if(GENERATED_DATASTRUCTURES_H MATCHES "immintrin\\.h")
            target_sources("${PERF_STEM}" PRIVATE tsc_x86.c)
            target_compile_options("${PERF_STEM}" PRIVATE -mavx2)
        endif()
    endif()
endforeach()
