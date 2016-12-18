import unittest
from main.day_20161216.palindrome import *


class PalindromeTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPalindrome(self):
        print(palindrome(121))

    if __name__ == '__main__':
        unittest.main()