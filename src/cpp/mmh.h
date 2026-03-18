#pragma once

// Generated for PrimeField(p=CrandallPrime(pi=130, theta=5)) (6x22 bits)

#include <stddef.h>
#include <stdint.h>

#include "configuration.h"
#include "helpers.h"

bigint_t mmh(bigint_t *R, bigint_t *M, uint64_t n) {
    bigint_t _1_acc =
        bigint_t{.limbs = {0x0UL, 0x0UL, 0x0UL, 0x0UL, 0x0UL, 0x0UL}};
    uint64_t i = 0;
    while (((i) < (((n) - (1))))) {
        _1_acc = _bigint_add(_1_acc, _bigint_mul(M[i], R[i]));
        i = ((i) + (1));
    }
    return _bigint_add(_1_acc, M[((n) - (1))]);
}
