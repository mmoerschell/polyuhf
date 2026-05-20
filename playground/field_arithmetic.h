#pragma once

#include <stddef.h>

#include "datastructures.h"

void op_add(bigint_t *dst, const bigint_t *lhs, const bigint_t *rhs);

void op_mul(bigint_t *dst, const bigint_t *lhs, const bigint_t *rhs);

void carry_round(bigint_t *x);

void load_le_bytes(bigint_t *dst, const uint8_t *src, const size_t n_src_bytes);

void store_le_bytes(uint8_t *dst, const size_t n_dst_bytes,
                    const bigint_t *src);
