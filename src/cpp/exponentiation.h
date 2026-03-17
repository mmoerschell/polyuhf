#pragma once

// Generated for PrimeField(p=CrandallPrime(pi=130, theta=5)) (6x22 bits)

#include <stddef.h>
#include <stdint.h>

#include "configuration.h"
#include "helpers.h"

bigint_t exponentiation(bigint_t base, uint64_t exponent) {
    return _bigint_exp(base, exponent);
}
