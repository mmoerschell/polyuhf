#include <math.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "generated/datastructures.h"
#include "generated/nmh.h"

#define B 1000
#define SEED 42
#define CHUNK_SIZE 14
#define NUM_WARMUP_ROUNDS 1000
#define NUM_MEASUR_ROUNDS 9000

int compare_doubles(const void *a, const void *b) {
    const double da = *(const double *)a;
    const double db = *(const double *)b;

    if (da < db) return -1;
    if (da > db) return 1;
    return 0;
}

uint64_t nanos(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ULL + ts.tv_nsec;
}

// int main(int argc, char **argv) {
int main(void) {
    const size_t buffer_len = B * CHUNK_SIZE;
    if (B & 7ll) {
        fprintf(stderr, "B must be a multiple of 8\n");
        return EXIT_FAILURE;
    }
    uint8_t *message = (uint8_t *)malloc(buffer_len);
    uint8_t *key = (uint8_t *)malloc(buffer_len);
    if (!message || !key) {
        fprintf(stderr, "Could not allocate message or key buffer\n");
        return EXIT_FAILURE;
    }
    srand(SEED);
    for (size_t i = 0; i < buffer_len; ++i) {
        message[i] = rand() & 255u;
        key[i] = rand() & 255u;
    }

    uint64_t sink = 0;
    for (size_t i = 0; i < NUM_WARMUP_ROUNDS; ++i) {
        const bigint_t res = nmh(message, key, B);
        sink ^= res.limb0;
    }

    double measured_min = 10000.0;
    double* samples = (double*) malloc(NUM_MEASUR_ROUNDS * sizeof(double));
    if (!samples) {
        fprintf(stderr, "Could not allocate samples buffer\n");
        return EXIT_FAILURE;
    }
    for (size_t i = 0; i < NUM_MEASUR_ROUNDS; ++i) {
        const uint64_t start = nanos();
        const bigint_t res = nmh(message, key, B);
        const uint64_t end = nanos();
        sink ^= res.limb0;
        samples[i] = (double)(end - start) / 1000000;
        measured_min = fmin(measured_min, samples[i]);
    }
    printf("min: %fns\n", measured_min);
    qsort(samples, NUM_MEASUR_ROUNDS, sizeof(double), compare_doubles);
    printf("mean: %fns\n", samples[NUM_MEASUR_ROUNDS / 2]);

    free(message);
    free(key);
    free(samples);
    fprintf(stderr, "", sink);
    return EXIT_SUCCESS;
}
