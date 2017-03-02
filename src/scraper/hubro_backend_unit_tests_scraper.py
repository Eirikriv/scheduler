import unittest

from massageItslearningData import *


class massageItslearningDataTester(unittest.TestCase):
    def test1(self): #testing mounthConverter for right dates
    	months=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
        counter = 1
        for month in months:
        	self.assertEqual(monthConverter(month), counter)
        	counter +=1

    def test2(self): #testing mounthConverter for wrong dates
    	incorretcMonths=["jan", "feb" ,"January","Janu"]
    	for incorretcMonth in incorretcMonths:
    		self.assertEqual(monthConverter(incorretcMonth),"00")
    
    #def test3(self): # testing getDayOnRightFormat for valit inputs, need more work here
    #	days = ["01","31","15","7","3"]
    #	correctDays=["01","31","15","07","03"]
    #	for n in range(len(days)-1):
    #		self.assertEqual(getDayOnRightFormat(days[n]),correctDays[n])


if __name__ == '__main__':
    unittest.main()