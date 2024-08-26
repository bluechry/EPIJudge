from test_framework import generic_test


# Solution 1: Shift and Mask
def parity_1(x: int) -> int:
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity


# Solution 2: Remove the Lowest Set Bit Repeatedly
def parity_2(x: int) -> int:
    parity = 0
    while x:
        parity ^= 1
        x &= x - 1
    return parity


# Solution 3: Precompute and Combine the Parity Bits of the Subgroups
parity_table = []


def make_parity_table(n: int) -> None:
    global parity_table

    for i in range(n):
        parity_table.append(parity_2(i))


def parity_3(x: int) -> int:
    mask = (1 << 8) - 1
    parity = 0
    while x:
        parity ^= parity_table[x & mask]
        x >>= 8
    return parity


# Solution 4: Repeatedly Xor the Two Halveds of the Integer
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
