import unittest
import sumnk


class TestSumNK(unittest.TestCase):

    def test_solvable(self):
        self.assertEqual(
            sumnk.find_sum(3, 51, [7, 3, 6, 10, 43, 54, 2]),
            [2, 6, 43])

    def test_not_solvable(self):
        self.assertIsNone(sumnk.find_sum(3, 51, [7, 3, 6]))
            

if __name__ == '__main__':
    unittest.main()