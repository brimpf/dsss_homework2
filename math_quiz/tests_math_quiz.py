import unittest
from math_quiz import rand_int, rand_op, calculate


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Value: {rand_num} was not in the specified range")

    def test_rand_op(self):
        # Test if random operators are either '+', '-', '*'
        for _ in range(50):  # Tests the randomization a number of times
            rand_operator = rand_op()
            self.assertIn(rand_operator, ['+', '-', '*'], f"0perator was {rand_operator}")

    def test_calculate(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 1, '+', '8 + 1', 9),
            (7, 3, '+', '7 + 3', 10),
            (10, 6, '+', '10 + 6', 16),
            (4, 9, '+', '4 + 9', 13),

            (5, 2, '-', '5 - 2', 3),
            (8, 1, '-', '8 - 1', 7),
            (7, 3, '-', '7 - 3', 4),
            (10, 6, '-', '10 - 6', 4),
            (4, 9, '-', '4 - 9', -5),

            (5, 2, '*', '5 * 2', 10),
            (8, 1, '*', '8 * 1', 8),
            (7, 3, '*', '7 * 3', 21),
            (10, 6, '*', '10 * 6', 60),
            (4, 9, '*', '4 * 9', 36),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"calculated problem: {problem} "
                                                        f"differed from the expected problem: {expected_problem}")
            self.assertEqual(answer, expected_answer, f"calculated answer: {answer} "
                                                      f"differed from the expected answer: {expected_answer}")


if __name__ == "__main__":
    unittest.main()
