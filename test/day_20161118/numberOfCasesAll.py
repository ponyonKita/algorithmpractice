import unittest



from main.day_20161118.numberOfCasesAll import *



class NumOfCases(unittest.TestCase):



    def setUp(self):

        pass



    def tearDown(self):

        pass



    def testGetNumberOfCasesAll(self):

       result = numberOfCasesAll(3)
       print(result)




if __name__ == '__main__':

    unittest.main()