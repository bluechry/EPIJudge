from test_framework import generic_test


# Solution 1: Shift and Mask
def parity_1(x: int) -> int:
    return 0


# Solution 2: Remove the Lowest Set Bit Repeatedly
def parity_2(x: int) -> int:
    return 0


# Solution 3: Precompute and Combine the Parity Bits of the Subgroups
def parity_3(x: int) -> int:
    return 0


# Solution 4: Repeatedly Xor the Two Halves of the Integer
def parity_4(x: int) -> int:
    return 0


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
