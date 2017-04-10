import unittest
import prime_factors


class TestPrimeFactors(unittest.TestCase):

    def test_simple_data(self):
        self.assertEqual(prime_factors.prime_factors(2), [2])
        self.assertEqual(prime_factors.prime_factors(10), [2, 5])
        self.assertEqual(prime_factors.prime_factors(16), [2, 2, 2, 2])
    
    def test_large_data(self):
        large_prime = 24036583
        self.assertEqual(prime_factors.prime_factors(large_prime), 
                         [large_prime])
        self.assertEqual(prime_factors.prime_factors(large_prime * large_prime),
                         [large_prime, large_prime])

    def test_bad_data(self):
        self.assertIsNone(prime_factors.prime_factors(0), None)
        self.assertIsNone(prime_factors.prime_factors(1), None)
        self.assertIsNone(prime_factors.prime_factors(-1000), None)
            

if __name__ == '__main__':
    unittest.main()
