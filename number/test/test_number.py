import unittest
from functools import reduce

import number.number as number


class TestNumber(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(number.lcm(12, 20), 60)
        self.assertEqual(reduce(number.lcm, [3, 12, 20]), 60)
        self.assertEqual(reduce(number.lcm, [40, 12, 20]), 120)
        self.assertEqual(reduce(number.lcm, list(range(1, 6)) + [20]), 60)


def load_tests(loader, tests, ignore):
    import doctest
    tests.addTests(doctest.DocTestSuite(number))
    return tests


if __name__ == '__main__':
    unittest.main()
