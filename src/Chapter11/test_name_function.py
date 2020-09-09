
import unittest
from name_function import get_formatted_name


class NameTestCase (unittest.TestCase):
	"""Test for the name funtion"""

	def test_first_last_name (self):
		"""testing formatted names"""

		formatted_name = get_formatted_name('Bob', 'Crow')
		self.assertEqual ('Bob Crow', formatted_name)


if __name__ == '__main__':
	unittest.main()

