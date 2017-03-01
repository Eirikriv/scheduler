import unittest

from massageItslearningData import *
def fun(x):
    return x + 1

class massageItslearningDataTester(unittest.TestCase):
    def test1(self): #testing mounthConverter for right dates
    	mounths=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
        counter = 1
        for mounth in mounths:
        	self.assertEqual(mounthConverter(mounth), counter)
        	counter +=1

    def test2(self): #testing mounthConverter for wrong dates
    	incorretcMounths=["jan,feb,January,Janu"]
    	for incorretcMounth in incorretcMounths:
    		self.assertEqual(mounthConverter(incorretcMounth),"00")
    
    def test3(self): # testing getDayOnRightFormat for valit inputs, need more work here
    	days = ["01","31","15","7","3"]
    	correctDays=["01","31","15","07","03"]
    	for n in range(len(days)-1):
    		self.assertEqual(getDayOnRightFormat(days[n]),correctDays[n])


if __name__ == '__main__':
    unittest.main()