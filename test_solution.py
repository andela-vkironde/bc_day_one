import unittest
from prime_no_solution import gen_prime_number

class Solution(unittest.TestCase):
	def test_n_is_seven(self):
		value = gen_prime_number(7)
		self.assertEqual(gen_prime_number(7), value)

if __name__ == "__main__":
    unittest.main()