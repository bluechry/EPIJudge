from test_framework import generic_test


# Solution 1: Find and toggle the rightmost 01 or 10 bits.
def closest_int_same_bit_count_1(x: int) -> int:
    num_bits = 64
    for i in range(num_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            bitmask = (1 << i) | (1 << (i + 1))
            return x ^ bitmask

    raise ValueError("All bits are 0 or 1.")


# Solution 2: Toggle the rightmost 01 or 10 bits in O(1).
def closest_int_same_bit_count_2(x: int) -> int:
    if x == 0 or x == (1 << 64) - 1:
        raise ValueError("All bits are 0 or 1.")

    # Find the rightmost set bit. If the rightmost set bit is the LSB, find the
    # rightmoset unset bit.
    flip_bit = x & ~(x - 1)
    if flip_bit == 1:
        flip_bit = ~x & (x + 1)

    # Toggle the rightmost '10' or '01' bits.
    bitmask = flip_bit | (flip_bit >> 1)
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
