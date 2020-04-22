"""
Set of functions for performing operations on numbers
"""


def exact_sqrt(x):
    """Calculate the square root of an arbitrarily large integer.

    The result of exact_sqrt(x) is a tuple (a, r) such that a**2 + r = x, where
    a is the largest integer such that a**2 <= x, and r is the "remainder".  If
    x is a perfect square, then r will be zero.

    Around two orders slower than math.sqrt!

    The algorithm used is the "long-hand square root" algorithm, as described at
    http://mathforum.org/library/drmath/view/52656.html
    """

    N = 0  # Problem so far
    a = 0  # Solution so far

    # We'll process the number two bits at a time, starting at the MSB
    L = x.bit_length()
    L += (L % 2)  # Round up to the next even number

    for i in range(L, -1, -1):

        # Get the next group of two bits
        n = (x >> (2 * i)) & 0b11

        # Check whether we can reduce the remainder
        if ((N - a * a) << 2) + n >= (a << 2) + 1:
            b = 1
        else:
            b = 0

        a = (a << 1) | b  # Concatenate the next bit of the solution
        N = (N << 2) | n  # Concatenate the next bit of the problem

    return a, N - a * a


def factorial(n):
    """Factorial of n without memoization. Can be used for calculation for very large numbers

    :param n (int): number to calculate for
    :return:
        n * (n-1) * (n-2) * ... * 1
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def cached_factorial(n: int) -> int:
    """Factorial of n, uses memoization of all previously calculated results. Useful if you need
    a lot of calculations for not so large numbers.

    :param n (int): number to calculate for
    :return:
        n * (n-1) * (n-2) * ... * 1
    """
    try:
        if n < len(cached_factorial.cache):
            return cached_factorial.cache[n]
    except AttributeError:
        cached_factorial.cache = [1, 1]
    cache_size = len(cached_factorial.cache)
    largest_in_cache = cached_factorial.cache[cache_size - 1]
    for i in range(cache_size, n + 1):
        largest_in_cache *= i
        cached_factorial.cache.append(largest_in_cache)
    return largest_in_cache


if __name__ == "__main__":
    import doctest
    from timeit import default_timer

    doctest.testmod()
    start_time = default_timer()
    # assert math.factorial(large_number) == factorial(large_number)
    import math

    # for i in range(0, 1000):
    #     gold_standard = math.factorial(i)
    #     assert gold_standard == cached_factorial(i) == factorial(i)
    #
    # large_number = 9999
    # assert math.factorial(large_number) == factorial(large_number)
    #
    # end_time = default_timer()
    # print("Execution time: {:.3f}s".format(end_time - start_time))
    very_large_number = 99999999999999

    second_run = default_timer()
    for i in range(1000):
        int(math.sqrt(very_large_number))
    end_second_run = default_timer()
    print("Execution time, math.sqrt: {:.3f}s".format(end_second_run - second_run))

    first_run = default_timer()
    for i in range(1000):
        exact_sqrt(very_large_number)
    end_first_run = default_timer()  #
    print("Execution time, exact_sqrt: {:.3f}s".format(end_first_run - first_run))
