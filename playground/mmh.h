#pragma once

#include <stdalign.h>
#include <stddef.h>
#include <stdint.h>

typedef union {
    alignas(64) uint64_t limbs[5];
} bigint_t1;

bigint_t1 mmh(uint8_t *message, uint8_t *key, int32_t B);
