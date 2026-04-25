import math
from typing import List


def det_sequence(seed: int, n: int):
    assert seed.bit_length() >= 32, f"Seed {seed:x} has bit length {seed.bit_length()}"
    for i in range(n):
        yield ((i * seed >> 24) ^ (0xAA if i & 1 else 0x55)) & 0xFF


PRIME = (1 << 116) - 3
BYTES_PER_FIELD_ELEMENT = 14


def mmh(message: List[int], key: List[int]) -> bytes:
    assert len(message) == len(key)
    B = math.ceil(len(message) / BYTES_PER_FIELD_ELEMENT)
    acc = 0
    for i in range(2):
    # for i in range(B - 1):
        Mi = int.from_bytes(
            message[i * BYTES_PER_FIELD_ELEMENT : (i + 1) * BYTES_PER_FIELD_ELEMENT],
            "little",
            signed=False,
        )
        ri = int.from_bytes(
            key[i * BYTES_PER_FIELD_ELEMENT : (i + 1) * BYTES_PER_FIELD_ELEMENT],
            "little",
            signed=False,
        )
        acc = (acc + Mi * ri) % PRIME
    # Mb = int.from_bytes(
    #     message[(B - 1) * BYTES_PER_FIELD_ELEMENT :], "little", signed=False
    # )
    # acc = (acc + Mb) % PRIME
    return acc.to_bytes(BYTES_PER_FIELD_ELEMENT + 1, "little", signed=False)


tests = [
    (mmh, 0xBAADF00D, 0xCAFEBABE, 16000),
    (mmh, 0xDEADBEEF, 0xFEEDFACE, 16000),
    (mmh, 0xBAADC0DE, 0xFACEFEED, 16000),
]

# print(" ".join(map(str, det_sequence(0xbaadf00d, 15))))
# print(" ".join(map(str, det_sequence(0xcafebabe, 15))))

for hash_f, message_seed, key_seed, length in tests:
    print(
        hash_f(
            list(det_sequence(message_seed, length)),
            list(det_sequence(key_seed, length)),
        ).hex()
    )
