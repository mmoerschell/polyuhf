#pragma once

#include <stddef.h>
#include <stdint.h>

void poly1305_ref(uint8_t *tag_, const uint8_t *key_, const uint8_t *message_,
              const size_t M_);
