from test_framework import generic_test


# Solution 1: Extract Each Bit and Place It in the Opposite Position
def reverse_bits_1(x: int) -> int:
    pass


# Solution 2: Swap Each Symmetric Bit Pair
def reverse_bits_2(x: int) -> int:
    pass


# Solution 3: Precompute and Reorder the Reversal of the Subgroups
def reverse_bits_3(x: int) -> int:
    pass


if __name__ == '__main__':

    # Test Solution 1
    generic_test.generic_test_main(
        'reverse_bits.py',
        'reverse_bits.tsv',
        reverse_bits_1
    )

    # Test Solution 2
    generic_test.generic_test_main(
        'reverse_bits.py',
        'reverse_bits.tsv',
        reverse_bits_2
    )

    # Test Solution 3
    generic_test.generic_test_main(
        'reverse_bits.py',
        'reverse_bits.tsv',
        reverse_bits_3
    )
