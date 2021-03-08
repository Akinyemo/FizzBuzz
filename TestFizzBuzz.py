import unittest
import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_mult_three(self):
        self.assertEqual(FizzBuzz.TestFizzBuzz(3),"Fizz")

     def test_mult_five(self):
        self.assertEqual(FizzBuzz.TestFizzBuzz(35),"Buzz")
        
if __name__ == "__main__":
    unittest.main()