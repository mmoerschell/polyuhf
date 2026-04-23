#include <stddef.h>
#include <string.h>

#include "datastructures.h"
#include "field_arithmetic.h"


inline bigint_t _bigint_add(const bigint_t lhs, const bigint_t rhs) {
    bigint_t dst;
    for (size_t i = 0; i < LIMBS; ++i)
        dst.limbs[i] = lhs.limbs[i] + rhs.limbs[i];
    return dst;
}

// Aliasing-safe
void op_add(bigint_t *dst, const bigint_t *lhs, const bigint_t *rhs) {
    for (size_t i = 0; i < LIMBS; ++i)
        dst->limbs[i] = lhs->limbs[i] + rhs->limbs[i];
}

void carry_round(bigint_t *x) {
    for (size_t i = 0; i < LIMBS - 1; ++i) {
        x->limbs[i + 1] += x->limbs[i] >> LAMBDA;
        x->limbs[i] &= LAMBDA_MASK;
    }
    x->limbs[0] += THETA * (x->limbs[LIMBS - 1] >> LAMBDA_PRIME);
    x->limbs[LIMBS - 1] &= LAMBDA_PRIME_MASK;
    for (size_t i = 0; i < 2; ++i) {
        x->limbs[i + 1] += x->limbs[i] >> LAMBDA;
        x->limbs[i] &= LAMBDA_MASK;
    }
}

void load_le_bytes(bigint_t *dst, const uint8_t *src,
                   const size_t n_src_bytes) {
    for (size_t i = 0; i < LIMBS; ++i)
        dst->limbs[i] = 0ull;
    for (size_t i = 0; i < n_src_bytes; ++i)
        dst->limbs[i * 8 / LAMBDA] |= src[i] << (i * 8 % LAMBDA);
}

void store_le_bytes(uint8_t *dst, const size_t n_dst_bytes,
                    const bigint_t *src) {
    memset(dst, 0, n_dst_bytes);
    for (size_t i = 0; i < n_dst_bytes; ++i) {
        const size_t global_bit_idx = 8 * i;
        const size_t limb_idx = global_bit_idx / LAMBDA;
        const size_t local_bit_idx = global_bit_idx % LAMBDA;
        dst[i] |= (uint8_t)(src->limbs[limb_idx] >> local_bit_idx);
        if (limb_idx + 1 < LIMBS) {
            dst[i] |=
                (uint8_t)(src->limbs[limb_idx + 1] << (LAMBDA - local_bit_idx));
        }
    }
}
