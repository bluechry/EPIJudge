from test_framework import generic_test


# Solution 1: Find and Toggle the Rightmost 01 or 10 Bits
def closest_int_same_bit_count_1(x: int) -> int:
    num_bits = 64
    for i in range(num_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            bitmask = (1 << i) | (1 << (i + 1))
            return x ^ bitmask

    raise ValueError("All bits are 0 or 1.")


# Solution 2: Toggle the Rightmost 01 or 10 Bits in O(1)
def closest_int_same_bit_count_2(x: int) -> int:
    # Find the rightmost '10' or '01' bit pair.
    # Start by finding the rightmost set bit.
    # If the LSB is 1, find the rightmost clear bit followed by a set bit.
    pos = x & ~(x - 1)
    if pos == 1:
        pos = ~x & (x + 1)

    # Toggle the rightmost '10' or '01' bits.
    bitmask = pos | (pos >> 1)
    return x ^ bitmask


if __name__ == '__main__':
    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_1
    )

    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_2
    )
