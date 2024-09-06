from test_framework import generic_test


# Solution 3: Toggle the Rightmost 01 or 10 Bits in O(1) 
def closest_int_same_bit_count_3(x: int) -> int:
    # Find the righmost '...10...0' subsequence.
    # 'pos' points the rightmost 1.
    pos = x & ~(x - 1)

    # If there is no '...10...0' subsequence,
    # find the rightmost '...01...1' subsequnece.
    # 'pos' points the rightmost 0.
    if pos == 1:
        pos = ~x & (x + 1)

    # Toggle '10' or '01' bits
    bitmask = pos | (pos >> 1)
    return x ^ bitmask


if __name__ == '__main__':
    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_3
    )
