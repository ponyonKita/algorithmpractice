import unittest
import time
from main.day_20161118.numberOfCasesAll import *


class numberOfCasesAllTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testgetNumberCase(self):
        result = getNumberCase(3)
        self.assertEqual(result, 7)

    if __name__ == '__main__':
        unittest.main()