import unittest
import time
from main.day_20161212.cardGame import *


class cardGameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testgetNumberCase(self):
        result = cardGame()
        print(result)

    if __name__ == '__main__':
        unittest.main()