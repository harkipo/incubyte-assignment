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

    def test_with_minus_signs_as_delimiter(self):  ## OK
        self.assertEqual( calculator.add('//-\n1-2'), 3)

    def test_rejects_negative_numbers(self):
        self.assertRaises(ValueError, calculator.add, '-2')
        self.assertRaises(ValueError, calculator.add, '-1,-2')




if __name__ == '__main__':
    unittest.main()

