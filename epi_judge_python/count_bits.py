from test_framework import generic_test


# Solution 1: Shift and Mask
def count_bits_1(x: int) -> int:
    return 0


# Solution 2: Remove the Right-most Set Bit Repeatedly
def count_bits_2(x: int) -> int:
    return 0


# Solution 3: Pythonic Way
def count_bits_3(x: int) -> int:
    return 0


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
