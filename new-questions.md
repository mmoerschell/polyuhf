1. Safe to stick to byte-aligned limb sizes? For example, with 24 bits, for GF(2^116-3):
    - lambda = 24
    - lambda' = 10
    - kappa 6 bits, but 17 for GF(2^226-5)..., but paper says "In particular [9] identified GF(2116 − 3) as promising candidate..."

1. Automatic parameter selection or programmer?

1. ARM Neon does not have 64-bit truncating multplication (no vmulq_u64)

1. Delayed carry propagation... E.g. SQH fails after a few hundred blocks -> Paper page 21

1. When using fields such as GF(2^116-3) or GF(2^226-5), confirm that we split message at byte and not field width boundaries? Also, last field element is "zero-extended" ? Does the programmer need to provide additional memory ?

1. Loading... assumptions? Simplifications? Cheaper alternatives? Zero-filling? Extending? Deduce chunk size from field?

1. Practicalities: calls

1. HKM update?
1. Karatsuba multiplication?
1. Report contents?
