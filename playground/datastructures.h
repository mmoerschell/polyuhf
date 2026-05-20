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
#define KAPPA (THETA * (1ull << (LAMBDA - LAMBDA_PRIME)))
#define BYTES_PER_FIELD_ELEMENT (PI / 8ull)

typedef union {
    alignas(64) uint64_t limbs[LIMBS];
} bigint_t;
