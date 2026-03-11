#pragma once

// Generated for PrimeField(p=CrandallPrime(pi=130, theta=5)) (6x22 bits)

#include "configuration.h"
#include "helpers.h"
#include <stddef.h>
#include <stdint.h>
bigint_t addition(bigint_t a, bigint_t b) { return _bigint_add(a, b); }
