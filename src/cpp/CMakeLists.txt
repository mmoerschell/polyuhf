cmake_minimum_required(VERSION 3.20)
project(polyuhf LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

set(MODULE_NAME "" CACHE STRING "Module to compile")
if("${MODULE_NAME}" STREQUAL "")
    message(FATAL_ERROR "You must pass MODULE_NAME, e.g. -DMODULE_NAME=mmh")
endif()

option(CORRECTNESS "Build a correctness target" ON)
option(PERFORMANCE "Build a performance target" ON)
option(AVX2_FLAG "Set -mavx2 flag" OFF)

find_package(Boost CONFIG REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

set(CORRECTNESS_TARGET correctness_${MODULE_NAME})
set(PERFORMANCE_TARGET performance_${MODULE_NAME})

######################
# Correctness target #
######################

if(CORRECTNESS)

    set(CORRECTNESS_SOURCES
        main.cpp
        little_endian_hex.cpp
        generated/${MODULE_NAME}.c
        generated/datastructures.c
        # TODO put autotests back in
    )
    # Manual tests
    if("${MODULE_NAME}" STREQUAL "poly1305")
        message(STATUS "Including manual Poly1305 tests")
        list(APPEND CORRECTNESS_SOURCES poly1305_tests.cpp)
    else()
        list(APPEND CORRECTNESS_SOURCES generated/${MODULE_NAME}_autotests.cpp)
    endif()

    # TODO: HKM test

    add_executable(${CORRECTNESS_TARGET} ${CORRECTNESS_SOURCES})

    target_link_libraries(${CORRECTNESS_TARGET}
        PRIVATE
            Boost::json
            Boost::unit_test_framework
            ${OPENSSL_LIBRARIES}
    )

    target_include_directories(${CORRECTNESS_TARGET} PRIVATE
        ${OPENSSL_INCLUDE_DIR}
    )

    target_compile_options(${CORRECTNESS_TARGET} PRIVATE
        -Wall
        -Wextra
        -Wpedantic
        -Wno-unused-variable
    )

    if(AVX2_FLAG)
        target_compile_options(${CORRECTNESS_TARGET} PRIVATE -mavx2)
    endif()
endif()

######################
# Performance target #
######################

if(PERFORMANCE)
    add_executable(${PERFORMANCE_TARGET}
        generated/${MODULE_NAME}_perf.c
        generated/${MODULE_NAME}.c
        generated/datastructures.c
    )

    target_compile_options(${PERFORMANCE_TARGET} PRIVATE
        # TODO find some better flags
        -O3
        -Wall
        -Wextra
        -Wpedantic
        -Wno-format-zero-length
    )

    if(AVX2_FLAG)
        target_sources(${PERFORMANCE_TARGET} PRIVATE "tsc_x86.c")
        target_compile_options(${PERFORMANCE_TARGET} PRIVATE -mavx2)
    endif()
endif()
