#pragma once

#include <cstdint>

#include "configuration.h"
#include "helpers.h"

inline bigint_t from_le_bytes(const uint8_t *data, const size_t n) {
    bigint_t res{};
    for (size_t i = 0; i < n; ++i) {
        const size_t lsbit_idx = 8 * i;
        const size_t limb_idx = lsbit_idx / LAMBDA;
        const size_t in_limb_idx = lsbit_idx % LAMBDA;
        res.limbs[limb_idx] |= data[i] << in_limb_idx;
    }
    return _bigint_carry_round(res);
}

inline void to_le_bytes(uint8_t *dst, const size_t n, const bigint_t &bigint) {
    memset(dst, 0, n);
    for (size_t i = 0; i < n; ++i) {
        const size_t lsbit_idx = 8 * i;
        const size_t limb_idx = lsbit_idx / LAMBDA;
        const size_t in_limb_idx = lsbit_idx % LAMBDA;
        dst[i] |= static_cast<uint8_t>(bigint.limbs[limb_idx] >> in_limb_idx);
        if (limb_idx + 1 < LIMBS)
            dst[i] |= static_cast<uint8_t>(bigint.limbs[limb_idx + 1]
                                           << (LAMBDA - in_limb_idx));
    }
}

