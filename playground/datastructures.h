#pragma once

#include <stdalign.h>
#include <stdint.h>

#define PI 116ull
#define THETA 3ull

#define LAMBDA 24ull
#define LAMBDA_PRIME 20ull
#define LIMBS 5ull
#define LAMBDA_MASK ((1ull << LAMBDA) - 1ull)
#define LAMBDA_PRIME_MASK ((1ull << LAMBDA_PRIME) - 1ull)

#define TAG_SIZE 17ull

typedef union {
    alignas(64) uint64_t limbs[LIMBS];
} bigint_t;
