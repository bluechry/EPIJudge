from test_framework import generic_test


# Solution 1: Find the previous and next permutation.
def closest_int_same_bit_count_1(x: int) -> int:
    def swap_adjacent_bits(val: int, i: int) -> int:
        bit_mask = (1 << i) | (1 << (i + 1))
        return val ^ bit_mask

    num_bits = 64
    inf = float('inf')

    # Find the previous permutation. 
    for i in range(num_bits - 1):
        if ((x >> (i + 1)) & 1) == 1 and ((x >> i) & 1) == 0:
            prev_x = swap_adjacent_bits(x, i)
            break
    else:
        prev_x = inf

    # Find the next permutation.
    for i in range(num_bits - 1):
        if ((x >> (i + 1)) & 1) == 0 and ((x >> i) & 1) == 1:
            next_x = swap_adjacent_bits(x, i)
            break
    else:
        next_x = inf

    if next_x == inf and prev_x == inf:
        raise ValueError("All bits are 0 or 1.")

    return prev_x if abs(prev_x - x) < abs(next_x - x) else next_x


# Solution 2: Find and toggle the rightmost 01 or 10 bits.
def closest_int_same_bit_count_2(x: int) -> int:
    num_bits = 64
    for i in range(num_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            bitmask = (1 << i) | (1 << (i + 1))
            return x ^ bitmask

    raise ValueError("All bits are 0 or 1.")


# Solution 3: Toggle the rightmost 01 or 10 bits in O(1).
def closest_int_same_bit_count_3(x: int) -> int:
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

    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_3
    )
