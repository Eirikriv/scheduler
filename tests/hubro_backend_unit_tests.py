
import sys

sys.path.append("../src/scraper")

from massageItslearningData import *	

import unittest

class massageItslearningDataTester(unittest.TestCase):
    def test_monthConverter_all_months_correct_number(self):
        months=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
        counter = 1
        for month in months:
            self.assertEqual(monthConverter(month), counter)
            counter +=1

    def test_monthConverter_wrong_month_format_error_flag(self):
        incorretcMonths=["jan", "feb" ,"January","Janu"]
        for incorretcMonth in incorretcMonths:
            self.assertEqual(monthConverter(incorretcMonth),"00")
    
    def test_getDayOnRightFormat_sample_days_correct(self): 
        days = ["01","31","15",".7",".3"]
    	correctDays=["01","31","15","07","03"]
    	for n in range(len(days)-1):
    		self.assertEqual(getDayOnRightFormat(days[n]),correctDays[n])

    def test_getDayOnRightFormat_sample_days_incorrect_flagg(self):
    	days = ["0112","3121","1415",".417",".13f",1,"abba"]
    	correctDays=["00","00","00","00","00","00","00"]
    	for n in range(len(days)-1):
    		self.assertEqual(getDayOnRightFormat(days[n]),correctDays[n])


    def test_getMonthOnRightFormat(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()