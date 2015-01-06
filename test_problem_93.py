# Unit tests for Project Euler Problem 93

import unittest
from Problem_93 import most_consecutive_targets


class EulerProblem93Test(unittest.TestCase):

    def test_known_values(self):
        self.assertEqual(most_consecutive_targets(), [(1, 2, 5, 8), 43])


if __name__ == '__main__':
    unittest.main()
