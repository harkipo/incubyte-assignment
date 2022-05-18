from StringCalculator import StringCalculator
import unittest

calculator = StringCalculator()


class TestStringCalculator(unittest.TestCase):

    def test_returns_single_number(self):  
        self.assertEqual(calculator.add('0'), 0)
        self.assertEqual(calculator.add('1'), 1)


    def test_ideal_case(self):  
        self.assertEqual(calculator.add('3,6'), 9)
        self.assertEqual(calculator.add('4,8'), 12)

    def test_newlines_as_delimiter(self):
        self.assertEqual(calculator.add('2\n6'), 8)



if __name__ == '__main__':
    unittest.main()

