import unittest
from calc import Calc


class TestCalc(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Calc().sum(1, 2), 3)

    def test_sum2(self):
        self.assertEqual(Calc().sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
