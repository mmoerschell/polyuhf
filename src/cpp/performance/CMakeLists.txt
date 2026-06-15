cmake_minimum_required(VERSION 3.20)
project(polyuhf_performance LANGUAGES C)

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

set(PERF_MODULE "" CACHE STRING "Generated module to benchmark, for example mmh")
set(POLYUHF_CPP_DIR "${CMAKE_CURRENT_LIST_DIR}/..")

if(PERF_MODULE)
    set(GENERATED_PERF_SOURCES "${GENERATED_DIR}/${PERF_MODULE}_perf.c")
    if(NOT EXISTS "${GENERATED_PERF_SOURCES}")
        message(FATAL_ERROR "No generated perf source for PERF_MODULE=${PERF_MODULE}: ${GENERATED_PERF_SOURCES}")
    endif()
else()
    file(GLOB_RECURSE GENERATED_PERF_SOURCES CONFIGURE_DEPENDS "${GENERATED_DIR}/*_perf.c")
endif()

if(NOT GENERATED_PERF_SOURCES)
    message(FATAL_ERROR "No generated perf sources found in ${GENERATED_DIR}")
endif()

foreach(PERF_SOURCE ${GENERATED_PERF_SOURCES})
    get_filename_component(PERF_STEM "${PERF_SOURCE}" NAME_WE)
    string(REGEX REPLACE "_perf$" "" MODULE_NAME "${PERF_STEM}")
    set(MODULE_SOURCE "${GENERATED_DIR}/${MODULE_NAME}.c")

    if(NOT EXISTS "${MODULE_SOURCE}")
        message(FATAL_ERROR "Perf source ${PERF_SOURCE} has no matching module source ${MODULE_SOURCE}")
    endif()

    add_executable("${PERF_STEM}"
        "${MODULE_SOURCE}"
        "${PERF_SOURCE}"
        "${GENERATED_DIR}/datastructures.c"
    )

    target_include_directories("${PERF_STEM}" PRIVATE
        ${GENERATED_DIR}
        ${GENERATED_PARENT_DIR}
        ${POLYUHF_CPP_DIR}
    )

    target_compile_options("${PERF_STEM}" PRIVATE
        -Wall
        -Wextra
        -Wpedantic
        -Wno-format-zero-length
    )

    if(POLYUHF_NEEDS_AVX2)
        target_sources("${PERF_STEM}" PRIVATE "${POLYUHF_CPP_DIR}/tsc_x86.c")
        target_compile_options("${PERF_STEM}" PRIVATE -mavx2)
    endif()
endforeach()
