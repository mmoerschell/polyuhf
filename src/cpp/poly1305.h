#pragma once

// Generated for PrimeField(p=CrandallPrime(pi=130, theta=5)) (6x22 bits)

#include <stddef.h>
#include <stdint.h>

#include "configuration.h"
#include "helpers.h"

bigint_t poly1305(bigint_t r, bigint_t *blocks, uint64_t n_blocks) {
    bigint_t _1_acc =
        bigint_t{.limbs = {0x0UL, 0x0UL, 0x0UL, 0x0UL, 0x0UL, 0x0UL}};
    uint64_t i = 0;
    while (((i) < (n_blocks))) {
        _1_acc = _bigint_add(
            _1_acc,
            _bigint_mul(
                _bigint_exp(r, ((n_blocks) - (i))),
                _bigint_add(blocks[i],
                            bigint_t{.limbs = {0x0UL, 0x0UL, 0x0UL, 0x0UL,
                                               0x0UL, 0x40000UL}})));
        i = ((i) + (1));
    }
    return _1_acc;
}
