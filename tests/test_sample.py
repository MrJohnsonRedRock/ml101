import unittest

from src import sample


class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sample.add(1, 2), 3)
        self.assertEqual(sample.add(-1, 5), 4)

    def test_divide(self):
        self.assertAlmostEqual(sample.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sample.divide(1, 0)


if __name__ == "__main__":
    unittest.main()
