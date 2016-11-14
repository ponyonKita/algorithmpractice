import unittest



from main.day_20161114.numberOfCases import *



class NumOfCases(unittest.TestCase):



    def setUp(self):

        pass



    def tearDown(self):

        pass



    def testGetNumberOfCases(self):

       result = numberOfCases(5)
       print(result)
       self.assertEquals(result, 13)



if __name__ == '__main__':

    unittest.main()