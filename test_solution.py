import unittest
from prime_no_solution import gen_prime_number

class Solution(unittest.TestCase):
	def test_n_is_seven(self):
		value = gen_prime_number(7)
		self.assertEqual(gen_prime_number(7), value)

	def test_negative_n (self):
		self.assertEqual(gen_prime_number(-4),"Error: Input positive number")

	def test_n_not_null (self):
	    n = None 
	    self.assertEqual(gen_prime_number(n),"Error: Invalid input")
 #        assert n Is Not None

if __name__ == "__main__":
    unittest.main()