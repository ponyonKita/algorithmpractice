import unittest
from main.day_20170228 import findPalindrome


class FindPalindromeTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFindPalindrome(self):
        inputString = 'abab'
        count = findPalindrome.find(inputString)
        self.assertEqual(findPalindrome.find(inputString), 5)
        print('Return:', count)

        inputString = 'abacaba'
        count = findPalindrome.find(inputString)
        self.assertEqual(findPalindrome.find(inputString), 7)
        print('Return:', count)

        inputString = 'qwerty'
        count = findPalindrome.find(inputString)
        self.assertEqual(findPalindrome.find(inputString), 11)
        print('Return:', count)

        inputString = 'abdfhdyrbdbsdfghjkllkjhgfds'
        count = findPalindrome.find(inputString)
        self.assertEqual(findPalindrome.find(inputString), 38)
        print('Return:', count)

    if __name__ == '__main__':
        unittest.main()