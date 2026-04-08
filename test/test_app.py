import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from app import message


class AppTests(unittest.TestCase):
    def test_should_return_hello_message(self):
        self.assertEqual(message(), "Hello world!")


if __name__ == "__main__":
    unittest.main()