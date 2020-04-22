"""
Set of functions for performing operations on matrices
"""

import copy
from fractions import Fraction
from typing import List, Callable, TypeVar

TNum = TypeVar('TNum', int, float, Fraction)


def gauss(a: List[List[TNum]], b: List[List[TNum]], eps: float = 1.0 / (10 ** 10)) -> (float, List[List[TNum]]):
    """Calculate x matrix in equation ax=b. It is recommended to apply on items, supporting fractions.
    Applying on int matrices may lead to an incorrect result, because int / int = int, i.e. they will be truncated.
    Should work for matrices of any size.

    :param a: input matrix A (2D array)
    :param b: input matrix b (2D array)
    :param eps: optional parameter for avoiding division to zero
    :return:
        (determinant of a, x matrix)
    :raises
        ValueError if 'a' is a singular matrix
    """
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n, m = len(a), len(a[0])
    assert n >= m, "Solution is not possible if number of rows < number of columns. A:{}".format(a)
    n = min(n, m)
    p = len(b[0])

    determinant = 1
    for i in range(n - 1):
        max_row = i
        for j in range(i + 1, n):  # Find max pivot (leftmost nonzero entry, or leading coefficient)
            if abs(a[j][i]) > abs(a[max_row][i]):
                max_row = j
        if max_row != i:
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]
            determinant = -determinant
        if abs(a[i][i]) <= eps:
            raise ValueError('Input matrix A is a singular matrix, there a no solutions!')

        for j in range(i + 1, n):  # Eliminate values in column i
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]
    # Put the matrix into reduced row echelon form (back substitute)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        determinant *= a[i][i]
        if abs(determinant) <= eps:
            raise ValueError('Input matrix A is a singular matrix, there a no solutions!')
        t = 1 / a[i][i]
        for j in range(p):  # Normalize row i
            b[i][j] *= t
    return determinant, b


def invert(m: List[List]) -> List[List]:
    """Invert matrix by creating an identity matrix and applying gauss elimination

    :param m: input matrix nxp, n>=p
    :return:
        inverse matrix of m
    """
    n, p = len(m), len(m[0])
    assert n >= p, "No inverse matrix exists for m:{}".format(m)

    # generate identity matrix, 1's, where i==j, 0's otherwise
    b = [[int(i == j) for j in range(p)] for i in range(n)]
    # extract the appended matrix (kind of m2[m:,...]
    return gauss(m, b)[1]


def filled_matrix(p: int, q: int, fill_val=0) -> List[List]:
    """Create matrix of size p x q and fill it with fill_val
     
    :param p:   number of rows 
    :param q:   number of columns
    :param fill_val: every element of matrix is going to be equal fill_val
    :return: matrix of size p x q 
    """
    return [[fill_val] * q for _ in range(p)]


def matmul(a: List[List], b: List[List]) -> List[List]:
    """Multiply matrices a (nxp) and b [pxq]

    :param a: input matrix a
    :param b: input matrix b
    :return:
        matrix nxq
    """
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])

    assert p == p1, "Incompatible dimensions of a:{} and b:{}".format(a, b)

    result = filled_matrix(n, q)
    for i in range(n):
        for j in range(q):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(p))
    return result


def map_matrix(f: Callable, a: List[List]) -> List[List]:
    """Apply f function/operator on every element of a

    :param f: some function
    :param a: input matrix
    :return:
        result of map operations
    """
    return [list(map(f, v)) for v in a]


def to_rational_matrix(a: List[List[TNum]]) -> List[List[Fraction]]:
    """Convert elements of matrix to Fractions

    :param a: input Matrix
    :return:
        matrix of Fractions
    """
    return map_matrix(Fraction, a)


def test_case(result, answer):
    print(result)
    assert result == answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = [
        [2, 9, 4],
        [7, 5, 3],
        [6, 1, 8]
    ]
    b = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    det, c = gauss(a, b)
    assert map_matrix(round, matmul(a, c)) == b

    ar, br = to_rational_matrix(a), to_rational_matrix(b)
    det, cr = gauss(ar, br)

    assert map_matrix(round, matmul(ar, cr)) == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    a_inverse = invert(a)
    assert map_matrix(round, matmul(a, a_inverse)) == b
