"""
A module with auxiliary functions for working with all around numbers

"""

import itertools
import math
from collections import deque

from pzeug.number.prime import sieve_of_eratosthenes


def reverse(n):
    reversed_n = 0
    while n > 0:
        reversed_n = 10 * reversed_n + (n % 10)
        n //= 10
    return reversed_n


def is_palindrome(number):
    return number == reverse(number)


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


def binomial_coefficient(n: int, k: int) -> int:
    """Returns n choose k, number of ways to choose an unordered subset of k elements
     from a fixed set of n elements.

    Args:
        n: n elements
        k: k elements to choose
    """

    if k > n:
        raise ValueError("The following must be True: n >= k. Supplied n={}, k={}.".format(n, k))

    try:
        if (n, k) in binomial_coefficient.cache:
            return binomial_coefficient.cache[(n, k)]
    except AttributeError:
        binomial_coefficient.cache = {}

    def _binomial_coefficient(n: int, k: int) -> int:
        if k == 0 or n == k:
            return 1
        elif (n, k) in binomial_coefficient.cache:
            return binomial_coefficient.cache[(n, k)]
        result = _binomial_coefficient(n - 1, k) + _binomial_coefficient(n - 1, k - 1)
        binomial_coefficient.cache[(n, k)] = result
        return result

    return _binomial_coefficient(n, k)


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


def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate Least Common Multiple using Greatest Common Divisor function.

    Examples:
      >>> lcm(12,20)
      60
    """
    return a * b // gcd(a, b)


def largest_palindrome(min_factor, max_factor):
    """Find largest palindrome given range of factors [min_factor, max_factor]

    Consider the digits of P – let them be x, y and z.
    P must be at least 6 digits long since the palindrome 111111 = 143×777 – the product of two 3-digit integers.
    Since P is palindromic:
        P=100000x10000y1000z100z10yx
        P=100001x10010y1100z
        P=119091x910y100z
    Since 11 is prime, at least one of the integers a or b must have a factor of 11.
    So if a is not divisible by 11 then we know b must be. Using this information
    we can determine what values of b we check depending on a.
    """

    max_palindrome = 0
    max_a = 0
    max_b = 0
    for a in range(max_factor, min_factor - 1, -1):
        if a % 11 == 0:
            b = max_factor
            b_step = -1
        else:
            b = max_factor - max_factor % 11
            b_step = -11
        for k in range(b, a - 1, b_step):
            multiplication = a * k
            if multiplication <= max_palindrome:
                break
            if is_palindrome(multiplication):
                max_palindrome = a * k
                max_a = a
                max_b = k
    return max_palindrome, max_a, max_b

    def smallest_num_divisible_by_each_to(k):
        """Calculate smallest number that can be divided by each of the numbers from 1 to k without any remainder.
        """
        check_limit = int(math.sqrt(k))
        result = 1
        for prime in sieve_of_eratosthenes(k):
            if prime > check_limit:
                result *= prime
            else:
                degree = int(math.log10(k) / math.log10(prime))
                result *= (prime ** degree)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # import inspect
    # import sys
    # current_module = sys.modules[__name__]
    # print(inspect.getsource(current_module))
    import fractions

    print(gcd(27, 54))
    print(lcm(3, 7))
    print(fractions.Fraction(27, 54) / gcd(27, 54))
