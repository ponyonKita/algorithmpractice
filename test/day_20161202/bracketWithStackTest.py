import unittest
import time
from main.day_20161202.bracketWithStack import *


class bracketWithStackTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testgetNumberCase(self):
        result = bracketCheckWithStack('{{}')
        print(result)

    if __name__ == '__main__':
        unittest.main()