"""
A module with auxiliary functions for working with all around numbers

"""

import itertools
from collections import deque


def digits_in_number(number):
    while number:
        yield number % 10
        number //= 10


def digits_to_number(digits):
    number = 0
    for i, d in enumerate(reversed(digits)):
        number += d * 10 ** i
    return number


def combinations(n):
    for digits in set(itertools.permutations(digits_in_number(n))):
        degree = len(digits) - 1
        digit_sum = 0
        for digit in digits:
            digit_sum += digit * 10 ** degree
            degree -= 1
        yield digit_sum


def circulars(digits):
    digits = deque(digits)
    length = len(digits)
    for i in range(1, length):
        digits.rotate(1)
        degree = 0
        digit_sum = 0
        for digit in digits:
            digit_sum += digit * 10 ** degree
            degree += 1
        yield digit_sum


# def prim_root(n):
#     totient = tot(n)
#     roots = []
#     exp = len(totient)
#     for x in totient:
#         y = 1
#         while pow(x, y, n) != 1:
#             y += 1
#         if y == exp:
#             roots.append(x)
#     return roots
#
#
# def colliatz_len(n, prev_len=0):
#     if n == 1:
#         return prev_len + 1
#     if n in len_hash:
#         return prev_len + len_hash[n]
#
#     return colliatz_len(n // 2 if n % 2 == 0 else 3 * n + 1, prev_len + 1)


def colliatz_sequence(n):
    yield n
    if n != 1:
        yield from colliatz_sequence(n // 2 if n % 2 == 0 else 3 * n + 1)


if __name__ == "__main__":
    # baz.py
    import inspect
    import sys

    current_module = sys.modules[__name__]
    print(inspect.getsource(current_module))
