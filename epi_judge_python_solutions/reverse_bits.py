from test_framework import generic_test


# Solution 1: Extract Each Bit and Place It in the Opposite Position
def reverse_bits_1(x: int) -> int:
    result = 0

    for i in range(64):
        bit = (x >> i) & 1
        result |= bit << (63 - i)

    return result


# 아래의 code는 한 번에 하나의 bit만 shift하기 때문에, 위 코드보다
# 더 빨라 보일 수 있지만, 실제로는 거의 동일한 속도를 보인다.
# 왜냐하면, shift 연산의 성능은 shift하는 bit들의 개수와 상관 없기 때문이다.
#
# def reverse_bits_1(x: int) -> int:
#     result = 0
#
#     for i in range(63):
#         result |= (x & 1)
#         x >>= 1
#         result <<= 1
#
#     return result


# Solution 2: Swap Each Symmetric Bit Pair
def reverse_bits_2(x: int) -> int:
    i = 63
    j = 0

    while i > j:
        if (x >> i) & 1 != (x >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        i -= 1
        j += 1

    return x


# Solution 3: Precompute and Reorder the Reversal of the Subgroups

# REVERSE_TABLE is initially a variable during construction,
# but it is intended to be used as a constant.
# It is a lookup table for reversing bits in an 16-bit number,
# used to optimize bit-reversal operations.
REVERSE_TABLE = []


def reverse_16bits(x: int) -> int:
    i = 15
    j = 0

    while i > j:
        if (x >> i) & 1 != (x >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        i -= 1
        j += 1

    return x


def make_reverse_table(n: int) -> None:
    global REVERSE_TABLE

    for x in range(n):
        REVERSE_TABLE.append(reverse_16bits(x))


def reverse_bits_3(x: int) -> int:
    grp_1 = (x >> 48) & 0xffff
    grp_2 = (x >> 32) & 0xffff
    grp_3 = (x >> 16) & 0xffff
    grp_4 = x & 0xffff

    result = (
        REVERSE_TABLE[grp_1] |
        REVERSE_TABLE[grp_2] << 16 |
        REVERSE_TABLE[grp_3] << 32 |
        REVERSE_TABLE[grp_4] << 48
    )

    return result


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
    make_reverse_table(1 << 16)

    generic_test.generic_test_main(
        'reverse_bits.py',
        'reverse_bits.tsv',
        reverse_bits_3
    )
