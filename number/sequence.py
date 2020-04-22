"""
A module with auxiliary functions for working with [infinite] sequences

"""


def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        b = a + b
        a = b - a
        yield b


def pentagonal_numbers(n=1):
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def triangle_numbers(n=1):
    while True:
        yield n * (n + 1) // 2
        n += 1


def hexagonal_numbers(n=1):
    while True:
        yield n * (2 * n - 1)
        n += 1
