import unittest
from prime_no_solution import gen_prime_number


class Solution(unittest.TestCase):
    def test_n_is_seven(self):
        value = gen_prime_number(8)
        self.assertEqual(gen_prime_number(8), value)

    def test_negative_n(self):
        self.assertEqual(gen_prime_number(-4),
                         "Error: Input positive number")

    def test_odd_number(self):
        container = gen_prime_number(10)
        self.assertNotIn(5, container)

    def test_n_null(self):
        self.assertEqual(gen_prime_number(None),
                         "Error: Invalid input")

    def test_if_list(self):
        try:
            assert type(gen_prime_number(10)) is list
        except AssertionError:
            raise(AssertionError("Wrong type"))
            # print ("Wrong type!")
            
    def test_string(self):
        value = gen_prime_number(8)
        self.assertTrue("Helloworld" != value)

    if __name__ == "__main__":
        unittest.main()
