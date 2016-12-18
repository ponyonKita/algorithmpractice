import unittest
from main.day_20161219.interestingParty import *


class InterestingPartyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInterestringParty(self):
        first = ['variety', 'diversity', 'loquacity', 'courtesy']
        second = ['talking', 'speaking', 'discussion', 'meeting']
        print(first)
        print(second)
        party = InterestingParty()
        print('return :' ,+ party.bestInvitation(first, second))

    if __name__ == '__main__':
        unittest.main()