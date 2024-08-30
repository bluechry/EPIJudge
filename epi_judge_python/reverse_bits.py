from test_framework import generic_test


# Solution 1
def reverse_bits_1(x: int) -> int:
    pass


# Solution 2
def reverse_bits_2(x: int) -> int:
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
