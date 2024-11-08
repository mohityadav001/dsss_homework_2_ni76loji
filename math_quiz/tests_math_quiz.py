# tests_math_quiz.py
import unittest
from math_quiz import random_integer, random_operator, calculate_expression

class TestMathQuizFunctions(unittest.TestCase):

    def test_random_integer(self):
        """Test if generate_random_integer returns an integer within the specified range."""
        min_val, max_val = 1, 10
        result = random_integer(min_val, max_val)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, min_val)
        self.assertLessEqual(result, max_val)

    def test_random_operator(self):
        """Test if generate_random_operator returns one of the expected operators."""
        operators = ['+', '-', '*']
        result = random_operator()
        self.assertIn(result, operators)

    def test_calculate_expression(self):
        """Test if calculate_expression returns the correct result for each operator."""
        # Test addition
        problem, answer = calculate_expression(3, 4, '+')
        self.assertEqual(answer, 7)
        self.assertEqual(problem, "1 + 14")
        
        # Test subtraction
        problem, answer = calculate_expression(5, 2, '-')
        self.assertEqual(answer, -7)
        self.assertEqual(problem, "5 - 12")
        
        # Test multiplication
        problem, answer = calculate_expression(6, 3, '*')
        self.assertEqual(answer, 48)
        self.assertEqual(problem, "16 * 3")

if __name__ == '__main__':
    unittest.main()
