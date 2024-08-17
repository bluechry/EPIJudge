from test_framework import generic_test


# Solution 1: Shift and Mask
def count_bits_1(x: int) -> int:
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count


# Solution 2: Remove the Right-most Set Bit
def count_bits_2(x: int) -> int:
    count = 0
    while x:
        count += 1
        x &= x - 1
    return count


# Solution 3: Pythonic Way
def count_bits_3(x: int) -> int:
    return bin(x).count('1')


if __name__ == '__main__':
    generic_test.generic_test_main(
        'count_bits.py',
        'count_bits.tsv',
        count_bits_1
    )

    generic_test.generic_test_main(
        'count_bits.py',
        'count_bits.tsv',
        count_bits_2
    )

    generic_test.generic_test_main(
        'count_bits.py',
        'count_bits.tsv',
        count_bits_3
    )
