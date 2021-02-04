from parameterized import parameterized
import unittest

class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ["foo", "a", "a",],
        ["bar", "c", "c"],
        ["lee", "b", "b"],
    ])
    def test_sequence(self, name, a, b):
        self.assertEqual(a,b)

if __name__ == '__main__':
	unittest.main()