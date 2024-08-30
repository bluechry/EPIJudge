from test_framework import generic_test


# Solution 1: Flip i-th and j-the Bits if They Differ
def swap_bits(x, i, j):

    # Extract the i- and j-th bits, and see if they differ.
    if (x >> i) & 1 != (x >> j) & 1:
        # i- and j-th bits differ. We will swap them by flipping their values.
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0, we can perform the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
