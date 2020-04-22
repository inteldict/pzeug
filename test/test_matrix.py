import unittest

import matrix


class TestMatrix(unittest.TestCase):

    def test_gauss(self):
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
        det, c = matrix.gauss(a, b)

        self.assertEqual(matrix.map_matrix(round, matrix.matmul(a, c)), b)

        self.assertEqual(c, [
            [-0.10277777777777776, 0.18888888888888888, -0.019444444444444438],
            [0.10555555555555554, 0.02222222222222223, -0.061111111111111116],
            [0.0638888888888889, -0.14444444444444446, 0.14722222222222223]
        ])

        # A test case from wikipedia
        a = [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2],
        ]
        b = [[8], [-11], [-3]]
        det, c = matrix.gauss(a, b)
        self.assertEqual(matrix.map_matrix(round, c), [
            [2],
            [3],
            [-1],
        ])

        # another test example
        a = [
            [2, 3],
            [5, 7],
        ]
        b = [
            [11],
            [13]
        ]
        det, c = matrix.gauss(a, b)
        self.assertEqual(matrix.map_matrix(round, c), [[-38],
                                                       [29]
                                                       ])

        with self.assertRaises(ValueError):
            # An example with a singular matrix
            a = [
                [3, 6],
                [1, 2],
            ]
            b = [
                [1, 0],
                [0, 1],
            ]
            c = matrix.gauss(a, b)

    def test_invert(self):
        with self.assertRaises(ValueError):
            singular_matrices = [
                [[0, 0],
                 [0, 0]],
                [[0, 0],
                 [0, 1]],
                [[0, 0],
                 [1, 0]],
                [[0, 0],
                 [1, 1]],
                [[0, 1],
                 [0, 0]],
                [[0, 1],
                 [0, 1]],
                [[1, 0],
                 [0, 0]],
                [[1, 0],
                 [1, 0]],
                [[1, 1],
                 [0, 0]],
                [[1, 1],
                 [1, 1]],
            ]
            for a in singular_matrices:
                matrix.invert(a)


def load_tests(loader, tests, ignore):
    import doctest
    tests.addTests(doctest.DocTestSuite(matrix))
    return tests


if __name__ == '__main__':
    unittest.main()
