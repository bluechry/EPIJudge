from test_framework import generic_test


# Solution 1: Find the previous and next number with the same number of set
# bits as x.
def closest_int_same_bit_count_1(x: int) -> int:
    def swap_adjacent_bits(val: int, i: int) -> int:
        bit_mask = (1 << i) | (1 << (i + 1))
        return val ^ bit_mask

    num_bits = 64
    inf = float('inf')

    # Find the previous number.
    for i in range(num_bits - 1):
        if ((x >> (i + 1)) & 1) == 1 and ((x >> i) & 1) == 0:
            prev_x = swap_adjacent_bits(x, i)
            break
    else:
        prev_x = inf

    # Find the next number.
    for i in range(num_bits - 1):
        if ((x >> (i + 1)) & 1) == 0 and ((x >> i) & 1) == 1:
            next_x = swap_adjacent_bits(x, i)
            break
    else:
        next_x = inf

    if next_x == inf and prev_x == inf:
        raise ValueError("All bits are 0 or 1.")

    return prev_x if abs(prev_x - x) < abs(next_x - x) else next_x


# Solution 2: Find and toggle the rightmost 01 or 10 bits
def closest_int_same_bit_count_2(x: int) -> int:
    num_bits = 64
    for i in range(num_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            bitmask = (1 << i) | (1 << (i + 1))
            return x ^ bitmask

    raise ValueError("All bits are 0 or 1.")


# Solution 3: Toggle the rightmost 01 or 10 bits in O(1)
def closest_int_same_bit_count_3(x: int) -> int:
    if x == 0 or x == (1 << 64) - 1:
        raise ValueError("All bits are 0 or 1.")

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

    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_3
    )
