#include "tsc_x86.h"

void init_tsc(void) {
    ; // no need to initialize anything for x86
}

TIMESTAMP start_tsc(void) {
    tsc_counter start;
    #ifndef PERF
    CPUID();
    RDTSC(start);
    #endif
    return COUNTER_VAL(start);
}

TIMESTAMP stop_tsc(TIMESTAMP start) {
    tsc_counter end;
    #ifndef PERF
    RDTSC(end);
    CPUID();
    #endif 
    return COUNTER_VAL(end) - start;
}
