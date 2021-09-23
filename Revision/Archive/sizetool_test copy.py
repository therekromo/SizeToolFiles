import unittest

from sizetool import *
class TestSizetool(unittest.TestCase):

    def test_get_path_size(self):
        testcase = r"/Users/therekromo/Desktop/checks"
        expected = 43109
        self.assertEqual(get_path_size(testcase), expected)

    def test_conversion(self):
        testcase = (r"/Users/therekromo/Desktop/checks", 43109)
        expected = "/Users/therekromo/Desktop/checks 41KB"
        self.assertEqual(conversion(*testcase), expected)

    def test_emptydirectory(self):
        testcase = r"/Users/therekromo/Desktop/emptydirect"
        expected = 0
        self.assertEqual(get_path_size(testcase), expected)

    def test_multipledirectories(self):
        testcase = r"/Users/therekromo/Desktop/emptydirect" , r"/Users/therekromo/Desktop/checks"
        expected = 0 , 43109
        for directory, expected_value in zip(testcase, expected):
            self.assertEqual(get_path_size(directory), expected_value)


unittest.main()
