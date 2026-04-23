def deterministic_sequence(n: int):
    for i in range(n):
        yield ((i * 0xdeadbeef >> 24) ^ (0xaa if i & 1 else 0x55)) & 0xff

print(" ".join(map(str, deterministic_sequence(15))))
