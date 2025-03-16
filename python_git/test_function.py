import unittest
import functionpractice


class TestCubeFunction(unittest.TestCase):

	def test_that_multiply_function_exists(self):
		actual = functionpractice.multiply_two_numbers(4,5)
		result = 20
		self.assertEqual(actual, result)
