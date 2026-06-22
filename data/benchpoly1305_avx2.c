#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../src/cpp/measurements/tsc_x86.h"

#include <openssl/evp.h>

#define SEED 42
#define NUM_MEASURE_ROUNDS 10
// Adaptive # of samples (reps) taken per measuring round, and divided

static int compare_doubles(const void *a, const void *b)
{
    const double x = *(const double *)a;
    const double y = *(const double *)b;

    return (x > y) - (x < y);
}


typedef enum {
    MODE_MIN = 0,
    MODE_MEDIAN = 1
} IOMode;


int main(int argc, char **argv) {
    // Input
    if (argc != 5) {
        fprintf(stderr, "Usage: %s <start> <stop> <step> <I/O-mode:min|median>\nboth ends inclusive, and where each parameter is a byte length\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Parameters
    const size_t start = atoll(argv[1]);
    const size_t stop = atoll(argv[2]);
    const size_t step = atoll(argv[3]);
    IOMode mode;
    if (!strcmp(argv[4], "min"))
        mode = MODE_MIN;
    else if (!strcmp(argv[4], "median"))
        mode = MODE_MEDIAN;
    else {
        fprintf(stderr, "Invalid mode %s\n", argv[4]);
        return EXIT_FAILURE;
    }

    // Allocate memory
    const size_t buffer_len = stop + 500;
    uint8_t *message = (uint8_t *)calloc(buffer_len, 1);
    uint8_t *key = (uint8_t *)calloc(buffer_len, 1);
    double *measurements = (double*) malloc(NUM_MEASURE_ROUNDS * sizeof(double));
    if (!message || !key || !measurements) {
        fprintf(stderr, "Could not allocate message or key buffer. Arguments too large?\n");
        return EXIT_FAILURE;
    }
    srand(SEED);
    for (size_t i = 0; i < buffer_len; ++i) {
        message[i] = rand() & 255u;
        key[i] = rand() & 255u;
    }

    uint8_t output[16];
    uint64_t sink = 0;

    EVP_MAC *mac = EVP_MAC_fetch(nullptr, "POLY1305", nullptr);
    EVP_MAC_CTX *ctx = EVP_MAC_CTX_new(mac);


    const double target_ticks = 1e9;
    
    // For all requested sizes
    for (size_t bytes = start; bytes <= stop; bytes += step) {
        // Dynamically adapt # of reps to target, doubles as warmup
        size_t reps;
        for (reps = 1; reps < (1u << 20); reps *= 2) {
            
            const myInt64 start = start_tsc();
            
            for (size_t r = 0; r < reps; r++) {
                EVP_MAC_init(ctx, key, 32, NULL);
                EVP_MAC_update(ctx, message, stop);
                EVP_MAC_final(ctx, output, &sink, 32);
                sink ^= output[0];
            }
            
            const myInt64 ticks = stop_tsc(start);
            
            if (ticks >= target_ticks) {
                break;
            }
        }
        
        
        double min_cycles = 1ull << 52ull;
        for (size_t i = 0; i < NUM_MEASURE_ROUNDS; ++i) {
            // Start timer
            
            const myInt64 start = start_tsc();
            
            for (size_t j = 0; j < reps; ++j) {
                // Function call
                EVP_MAC_init(ctx, key, 32, NULL);
                EVP_MAC_update(ctx, message, stop);
                EVP_MAC_final(ctx, output, &sink, 32);
            }
            // Stop timer, estimate cycles
            
            const myInt64 sample = stop_tsc(start);
            const double cycles = (double)sample / reps;
            
            
            // Save result, update minimum
            measurements[i] = cycles;
            min_cycles = cycles < min_cycles ? cycles : min_cycles;
        }
        
        // Output
        if (mode == MODE_MIN) {
            printf("%.0f\n", min_cycles);
        } else if (mode == MODE_MEDIAN) {
            qsort(measurements, NUM_MEASURE_ROUNDS, sizeof(measurements[0]), compare_doubles);
            printf("%.0f\n", measurements[NUM_MEASURE_ROUNDS / 2]);
        }
        fflush(stdout);
        
    }
    
    EVP_MAC_CTX_free(ctx);
    EVP_MAC_free(mac);
    
    free(message);
    free(key);
    free(measurements);
    fprintf(stderr, "", sink);
    return EXIT_SUCCESS;
}
