#pragma once

// Generated for PrimeField(p=CrandallPrime(pi=130, theta=5)) (6x22 bits)

#include <stddef.h>
#include <stdint.h>

#include "configuration.h"
#include "helpers.h"

bigint_t addition(bigint_t a, bigint_t b) { return _bigint_add(a, b); }
