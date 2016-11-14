import unittest



from main.day_20161101.fibonacciSequence import *



class FibonacciSequenceTest(unittest.TestCase):



    def setUp(self):

        pass



    def tearDown(self):

        pass



    def testGetFibonacciNumberByIterate(self):

        self.assertEqual(getFibonacciNumberByIterate(0), 0)

        self.assertEqual(getFibonacciNumberByIterate(1), 1)

        self.assertEqual(getFibonacciNumberByIterate(2), 1)

        self.assertEqual(getFibonacciNumberByIterate(3), 2)

        self.assertEqual(getFibonacciNumberByIterate(4), 3)

        self.assertEqual(getFibonacciNumberByIterate(5), 5)




if __name__ == '__main__':

    unittest.main()