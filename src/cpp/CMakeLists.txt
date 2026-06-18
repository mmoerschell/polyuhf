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

find_package(Boost CONFIG REQUIRED COMPONENTS unit_test_framework json)
find_package(OpenSSL REQUIRED)

set(CORRECTNESS_TARGET correctness_${MODULE_NAME})
set(PERFORMANCE_TARGET performance_${MODULE_NAME})

#########
# Flags #
#########

set(PLATFORM "" CACHE STRING "Platform to build for: neon | avx2")
if("${PLATFORM}" STREQUAL "neon")
    set(C_BUILD_FLAGS
        # Warnings
        -Wall
        -Wextra
        -Wpedantic
        -Wno-unused-variable
        -Wno-format-zero-length
        # Performance
        -O3
        -DNDEBUG
        -mcpu=apple-m3 # NOTE alternatively: -mcpu=native
        -fomit-frame-pointer
    )
elseif("${PLATFORM}" STREQUAL "avx2")
    set(C_BUILD_FLAGS
        # Warnings
        -Wall
        -Wextra
        -Wpedantic
        -Wno-unused-variable
        -Wno-format-zero-length
        # Performance
        -O3
        -DNDEBUG
        -march=native # pulls in -mavx2
        -fomit-frame-pointer
        )
else()
    message(FATAL_ERROR "Invalid PLATFORM '${PLATFORM}'")
endif()


######################
# Correctness target #
######################

if(CORRECTNESS)

    set(CORRECTNESS_SOURCES
        main.cpp
        little_endian_hex.cpp
        generated/${MODULE_NAME}.c
        generated/datastructures.c
        generated/${MODULE_NAME}_autotests.cpp
    )

    # OpenSSL Poly1305 tests
    if("${MODULE_NAME}" STREQUAL "poly1305")
        message(STATUS "Including manual Poly1305 tests")
        list(APPEND CORRECTNESS_SOURCES poly1305_tests.cpp)
    endif()

    # HKM iterative rewrite tests
    if("${MODULE_NAME}" STREQUAL "hkm_iter")
        message(STATUS "Including HKM rewrite tests")
        list(APPEND CORRECTNESS_SOURCES hkm_tests.cpp)
    endif()

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

    target_compile_options(${CORRECTNESS_TARGET} PRIVATE ${C_BUILD_FLAGS})
endif()

######################
# Performance target #
######################

if(PERFORMANCE)
    add_executable(${PERFORMANCE_TARGET}
    generated/${MODULE_NAME}.c
    generated/datastructures.c
    generated/${MODULE_NAME}_perf.c
    )

    target_compile_options(${PERFORMANCE_TARGET} PRIVATE ${C_BUILD_FLAGS})
endif()
