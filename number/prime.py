import math
from functools import reduce


def sieve_of_eratosthenes(limit):
    uneven_limit = math.ceil(limit / 2) - 1
    a = [True] * uneven_limit  # Initialize the primality list
    yield 2
    i = 3
    crosslimit = int(math.sqrt(limit))
    for isprime in a:
        if isprime:
            yield i
            if i <= crosslimit:
                for n in range(i * i // 2 - 1, uneven_limit, i):  # Mark factors non-prime
                    a[n] = False
        i += 2


def sieve_of_factors(limit):
    limit += 1
    a = [0] * limit  # Initialize the count_factors_list
    i = factor = 2
    while i < limit:
        a[i] = 1
        i *= factor

    factor = 3
    while factor < limit:
        i = factor
        if a[i] == 0:
            while i < limit:
                a[i] = 1
                i *= factor
        factor += 2
    return a


def prime_factorizations(n):
    sieve = [[] for x in range(0, n)]
    for i in range(2, n):
        if not sieve[i]:
            q = i
            while q < n:
                for r in range(q, n, q):
                    sieve[r].append(i)
                q *= i
    return sieve


def sieve_of_factors2(n):
    sieve = [0 for x in range(0, n)]
    for i in range(2, n):
        if sieve[i] == 0:
            q = i
            while q < n:
                for r in range(q, n, q):
                    sieve[r] += 1
                q *= i
    return sieve


def pentagonal(n=1):
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def traingle(n=1):
    while True:
        yield n * (n + 1) // 2
        n += 1


def hexagonal(n=1):
    while True:
        yield n * (2 * n - 1)
        n += 1


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f += 6
        return True


def goldbach_conjecture(odd_composite):
    for i in itertools.count(1):
        diff = odd_composite - 2 * i * i
        if diff < 1:
            break
        if is_prime(diff):
            return True
    return False


def factors(n):
    factor = 2
    if n % factor == 0:
        n //= factor
        degree = 1
        while n % factor == 0:
            n //= factor
            degree += 1
        yield factor, degree

    factor = 3
    maxfactor = math.sqrt(n)
    while n > 1 and factor <= maxfactor:
        if n % factor == 0:

            n //= factor

            degree = 1
            while n % factor == 0:
                n //= factor
                degree += 1

            maxfactor = math.sqrt(n)
            yield factor, degree
        factor += 2
    if n != 1:
        yield n, 1


def count_factors(n):
    number_factors = 0
    factor = 2
    if n % factor == 0:
        number_factors = 1
        n //= factor
        while n % factor == 0:
            n //= factor

    factor = 3
    maxfactor = math.sqrt(n)
    while n > 1 and factor <= maxfactor:
        if n % factor == 0:
            number_factors += 1
            n //= factor
            while n % factor == 0:
                n //= factor
            maxfactor = math.sqrt(n)
        factor += 2
    if n != 1:
        number_factors += 1
    return number_factors


def factors(n):
    factor = 2
    if n % factor == 0:
        n //= factor
        degree = 1
        while n % factor == 0:
            n //= factor
            degree += 1
        yield factor, degree

    factor = 3
    maxfactor = math.sqrt(n)
    while n > 1 and factor <= maxfactor:
        if n % factor == 0:

            n //= factor

            degree = 1
            while n % factor == 0:
                n //= factor
                degree += 1

            maxfactor = math.sqrt(n)
            yield factor, degree
        factor += 2
    if n != 1:
        yield n, 1


def all_factors(n, start_at=1):
    return set(tuple(sorted(p)) for p in ((i, n // i) for i in range(start_at, int(n ** 0.5) + 1) if n % i == 0))


def find_prime_factors(k, all_primes):
    primes = tuple(prime for prime in all_primes if prime <= k and k % prime == 0)
    number_of_coefficients = len(primes)
    degrees = list(1 for x in range(number_of_coefficients))
    for i in range(number_of_coefficients):
        if primes[i] > math.sqrt(k):
            break
        degrees[i] = int(math.log(k, primes[i]))
    return zip(primes, degrees)


def factors(n):
    factor = 2
    if n % factor == 0:
        n //= factor
        degree = 1
        while n % factor == 0:
            n //= factor
            degree += 1
        yield factor, degree

    factor = 3
    maxfactor = math.sqrt(n)
    while n > 1 and factor <= maxfactor:
        if n % factor == 0:

            n //= factor

            degree = 1
            while n % factor == 0:
                n //= factor
                degree += 1

            maxfactor = math.sqrt(n)
            yield factor, degree
        factor += 2
    if n != 1:
        yield n, 1


def proper_divisors(n):
    if is_prime(n):
        return (1,)
    divisors = set(reduce(list.__add__, ([i, n // i] for i in range(2, int(n ** 0.5) + 1) if n % i == 0)))
    divisors.add(1)
    return divisors


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f += 6
        return True
