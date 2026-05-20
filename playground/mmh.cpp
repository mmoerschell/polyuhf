#include "mmh.h"

bigint_t1 mmh(uint8_t *message, uint8_t *key, int32_t B) {
    int32_t var0 = B - 1;
    bigint_t1 var1{0, 0, 0, 0, 0};
    for (int32_t i = 0; i < var0; i += 1) {
        // var2 = load message i
        bigint_t1 var2{};
        var2.limbs[0] |= message[(14 * i) + 0] << 0;
        var2.limbs[0] |= message[(14 * i) + 1] << 8;
        var2.limbs[0] |= message[(14 * i) + 2] << 16;
        var2.limbs[1] |= message[(14 * i) + 3] << 0;
        var2.limbs[1] |= message[(14 * i) + 4] << 8;
        var2.limbs[1] |= message[(14 * i) + 5] << 16;
        var2.limbs[2] |= message[(14 * i) + 6] << 0;
        var2.limbs[2] |= message[(14 * i) + 7] << 8;
        var2.limbs[2] |= message[(14 * i) + 8] << 16;
        var2.limbs[3] |= message[(14 * i) + 9] << 0;
        var2.limbs[3] |= message[(14 * i) + 10] << 8;
        var2.limbs[3] |= message[(14 * i) + 11] << 16;
        var2.limbs[4] |= message[(14 * i) + 12] << 0;
        var2.limbs[4] |= message[(14 * i) + 13] << 8;

        // var3 = load key i
        bigint_t1 var3{};
        var3.limbs[0] |= key[(14 * i) + 0] << 0;
        var3.limbs[0] |= key[(14 * i) + 1] << 8;
        var3.limbs[0] |= key[(14 * i) + 2] << 16;
        var3.limbs[1] |= key[(14 * i) + 3] << 0;
        var3.limbs[1] |= key[(14 * i) + 4] << 8;
        var3.limbs[1] |= key[(14 * i) + 5] << 16;
        var3.limbs[2] |= key[(14 * i) + 6] << 0;
        var3.limbs[2] |= key[(14 * i) + 7] << 8;
        var3.limbs[2] |= key[(14 * i) + 8] << 16;
        var3.limbs[3] |= key[(14 * i) + 9] << 0;
        var3.limbs[3] |= key[(14 * i) + 10] << 8;
        var3.limbs[3] |= key[(14 * i) + 11] << 16;
        var3.limbs[4] |= key[(14 * i) + 12] << 0;
        var3.limbs[4] |= key[(14 * i) + 13] << 8;

        bigint_t1 var4{};
        // var4 = mul var2 var3
        var4.limbs[0] += var2.limbs[0] * var3.limbs[0];
        var4.limbs[0] += var2.limbs[1] * 48 * var3.limbs[4];
        var4.limbs[0] += var2.limbs[2] * 48 * var3.limbs[3];
        var4.limbs[0] += var2.limbs[3] * 48 * var3.limbs[2];
        var4.limbs[0] += var2.limbs[4] * 48 * var3.limbs[1];
        var4.limbs[1] += var2.limbs[0] * var3.limbs[1];
        var4.limbs[1] += var2.limbs[1] * var3.limbs[0];
        var4.limbs[1] += var2.limbs[2] * 48 * var3.limbs[4];
        var4.limbs[1] += var2.limbs[3] * 48 * var3.limbs[3];
        var4.limbs[1] += var2.limbs[4] * 48 * var3.limbs[2];
        var4.limbs[2] += var2.limbs[0] * var3.limbs[2];
        var4.limbs[2] += var2.limbs[1] * var3.limbs[1];
        var4.limbs[2] += var2.limbs[2] * var3.limbs[0];
        var4.limbs[2] += var2.limbs[3] * 48 * var3.limbs[4];
        var4.limbs[2] += var2.limbs[4] * 48 * var3.limbs[3];
        var4.limbs[3] += var2.limbs[0] * var3.limbs[3];
        var4.limbs[3] += var2.limbs[1] * var3.limbs[2];
        var4.limbs[3] += var2.limbs[2] * var3.limbs[1];
        var4.limbs[3] += var2.limbs[3] * var3.limbs[0];
        var4.limbs[3] += var2.limbs[4] * 48 * var3.limbs[4];
        var4.limbs[4] += var2.limbs[0] * var3.limbs[4];
        var4.limbs[4] += var2.limbs[1] * var3.limbs[3];
        var4.limbs[4] += var2.limbs[2] * var3.limbs[2];
        var4.limbs[4] += var2.limbs[3] * var3.limbs[1];
        var4.limbs[4] += var2.limbs[4] * var3.limbs[0];

        // var1 = add var1 var4
        var1.limbs[0] = var1.limbs[0] + var4.limbs[0];
        var1.limbs[1] = var1.limbs[1] + var4.limbs[1];
        var1.limbs[2] = var1.limbs[2] + var4.limbs[2];
        var1.limbs[3] = var1.limbs[3] + var4.limbs[3];
        var1.limbs[4] = var1.limbs[4] + var4.limbs[4];
    }
    int32_t var5 = B - 1;
    // var6 = load message var5
    bigint_t1 var6{};
    var6.limbs[0] |= message[(14 * var5) + 0] << 0;
    var6.limbs[0] |= message[(14 * var5) + 1] << 8;
    var6.limbs[0] |= message[(14 * var5) + 2] << 16;
    var6.limbs[1] |= message[(14 * var5) + 3] << 0;
    var6.limbs[1] |= message[(14 * var5) + 4] << 8;
    var6.limbs[1] |= message[(14 * var5) + 5] << 16;
    var6.limbs[2] |= message[(14 * var5) + 6] << 0;
    var6.limbs[2] |= message[(14 * var5) + 7] << 8;
    var6.limbs[2] |= message[(14 * var5) + 8] << 16;
    var6.limbs[3] |= message[(14 * var5) + 9] << 0;
    var6.limbs[3] |= message[(14 * var5) + 10] << 8;
    var6.limbs[3] |= message[(14 * var5) + 11] << 16;
    var6.limbs[4] |= message[(14 * var5) + 12] << 0;
    var6.limbs[4] |= message[(14 * var5) + 13] << 8;

    bigint_t1 var7{};
    // var7 = add var1 var6
    var7.limbs[0] = var1.limbs[0] + var6.limbs[0];
    var7.limbs[1] = var1.limbs[1] + var6.limbs[1];
    var7.limbs[2] = var1.limbs[2] + var6.limbs[2];
    var7.limbs[3] = var1.limbs[3] + var6.limbs[3];
    var7.limbs[4] = var1.limbs[4] + var6.limbs[4];

    // carry var7
    var7.limbs[1] += var7.limbs[0] >> 24;
    var7.limbs[0] &= 16777215ull;
    var7.limbs[2] += var7.limbs[1] >> 24;
    var7.limbs[1] &= 16777215ull;
    var7.limbs[3] += var7.limbs[2] >> 24;
    var7.limbs[2] &= 16777215ull;
    var7.limbs[4] += var7.limbs[3] >> 24;
    var7.limbs[3] &= 16777215ull;
    var7.limbs[0] += 3 * (var7.limbs[4] >> 20);
    var7.limbs[4] &= 1048575ull;
    var7.limbs[1] += var7.limbs[0] >> 24;
    var7.limbs[0] &= 16777215ull;
    var7.limbs[2] += var7.limbs[1] >> 24;
    var7.limbs[1] &= 16777215ull;
    return var7;
}
