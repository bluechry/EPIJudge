from test_framework import generic_test


# Solution 1: Scan All Bits
def parity_1(x: int) -> int:
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity


# Solution 2: Check Set Bits
def parity_2(x: int) -> int:
    parity = 0
    while x:
        parity ^= 1
        x &= x - 1
    return parity


# Solution 3: Precompute the Parity Bits
parity_table = {}


def make_parity_table(n: int) -> dict:
    for i in range(n):
        parity_table[i] = parity_1(i)
    return parity_table


def parity_3(x: int) -> int:
    mask = (1 << 8) - 1
    parity = 0
    while x:
        parity ^= parity_table[x & mask]
        x >>= 8
    return parity


# Solution 4: Divide and Xor
def parity_4(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


if __name__ == '__main__':
    generic_test.generic_test_main(
        'parity.py',
        'parity.tsv',
        parity_1
    )

    generic_test.generic_test_main(
        'parity.py',
        'parity.tsv',
        parity_2
    )

    make_parity_table(1 << 8)
    generic_test.generic_test_main(
        'parity.py',
        'parity.tsv',
        parity_3
    )

    generic_test.generic_test_main(
        'parity.py',
        'parity.tsv',
        parity_4
    )
