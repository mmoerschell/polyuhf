#pragma once

// Generated for PrimeField(p=CrandallPrime(pi=130, theta=5)) (6x22 bits)

#include "configuration.h"
#include "helpers.h"
#include <stddef.h>
#include <stdint.h>
bigint_t exponentiation(bigint_t base, uint64_t exponent) {
    bigint_t _1_acc = base;
    uint64_t _2_i = 0;
    while (((_2_i) < (((exponent) - (1))))) {
        _1_acc = _bigint_mult(_1_acc, base);
        _2_i = ((_2_i) + (1));
    }
    return _1_acc;
}
