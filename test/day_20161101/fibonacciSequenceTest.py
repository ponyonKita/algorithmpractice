import unittest



from main.day_20161031.FibonacciSequence import *



class FibonacciSequenceTest(unittest.TestCase):



    def setUp(self):

        pass



    def tearDown(self):

        pass



    def testGetFibonacciNumberByIterate(self):

        self.assertEqual(getFibonacciNumberByIterate(1), 0)

        self.assertEqual(getFibonacciNumberByIterate(2), 1)

        self.assertEqual(getFibonacciNumberByIterate(3), 1)

        self.assertEqual(getFibonacciNumberByIterate(4), 2)

        self.assertEqual(getFibonacciNumberByIterate(5), 3)



    def testGetFibonacciNumberByRecursive(self):

        self.assertEqual(getFibonacciNumberByRecursive(1), 0)

        self.assertEqual(getFibonacciNumberByRecursive(2), 1)

        self.assertEqual(getFibonacciNumberByRecursive(3), 1)

        self.assertEqual(getFibonacciNumberByRecursive(4), 2)

        self.assertEqual(getFibonacciNumberByRecursive(5), 3)



if __name__ == '__main__':

    unittest.main()