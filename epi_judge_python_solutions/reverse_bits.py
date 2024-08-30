from test_framework import generic_test


# Solution 1
def reverse_bits_1(x: int) -> int:
    i = 63
    j = 0

    while i > j:
        if (x >> i) & 1 != (x >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        i -= 1
        j += 1

    return x


# Solution 2
REVERSE_TABLE = []  # Assume this reverse table is used as constant.


def reverse_16bits(x: int) -> int:
    i = 15
    j = 0

    while i > j:
        if (x >> i) & 1 != (x >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        i -= 1
        j += 1

    return x


def make_reverse_table(n: int) -> None:
    global REVERSE_TABLE

    for x in range(n):
        REVERSE_TABLE.append(reverse_16bits(x))


def reverse_bits_2(x: int) -> int:
    grp_1 = (x >> 48) & 0xffff
    grp_2 = (x >> 32) & 0xffff
    grp_3 = (x >> 16) & 0xffff
    grp_4 = x & 0xffff

    result = (
        REVERSE_TABLE[grp_1] |
        REVERSE_TABLE[grp_2] << 16 |
        REVERSE_TABLE[grp_3] << 32 |
        REVERSE_TABLE[grp_4] << 48
    )

    return result


if __name__ == '__main__':

    # Test Solution 1
    generic_test.generic_test_main(
        'reverse_bits.py',
        'reverse_bits.tsv',
        reverse_bits_1
    )

    # Test Solution 2
    make_reverse_table(1 << 16)

    generic_test.generic_test_main(
        'reverse_bits.py',
        'reverse_bits.tsv',
        reverse_bits_2
    )
