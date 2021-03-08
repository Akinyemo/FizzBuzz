import unittest
import FizzBuzz

#test for fizzbuzz
class TestFizzBuzz(unittest.TestCase):

    def test_mult_three(self):
        self.assertEqual(FizzBuzz.TestFizzBuzz(3),"Fizz")

    def test_mult_five(self):
        self.assertEqual(FizzBuzz.TestFizzBuzz(35),"Buzz")

    def test_mult_five_and_three(self):
        self.assertEqual(FizzBuzz.TestFizzBuzz(30),"FizzBuzz")
if __name__ == "__main__":
    unittest.main()