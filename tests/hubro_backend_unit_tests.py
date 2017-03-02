
import sys

sys.path.append("../src/scraper")

from massageItslearningData import *	
from readItslearningAssignments import *
import unittest

class massageItslearningDataTester(unittest.TestCase):
    def test_monthConverter_all_months_correct_number(self):
        months=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
        counter = 1
        for month in months:
            self.assertEqual(monthConverter(month), str(counter))
            counter +=1

    def test_monthConverter_wrong_month_format_error_flag(self):
        incorretcMonths=["jan", "feb" ,"January","Janu"]
        for incorretcMonth in incorretcMonths:
            self.assertEqual(monthConverter(incorretcMonth),"00")
    
    def test_getDateOnRightFormat_sample_days_correct(self): 
        days = ["01","31","15",".7",".3","12.","03"]
        correctDays=["01","31","15","07","03","12","03"]
    	for n in range(len(days)-1):
    		self.assertEqual(getDateOnRightFormat(days[n]),correctDays[n])

    def test_getDateOnRightFormat_sample_days_incorrect_flagg(self):
    	month = ["0112","3121","1415",".417",".13f",1,"abba","02","12"]
    	correcktMonth=["00","00","00","00","00","00","00","02","12"]
    	for n in range(len(month)-1):
    		self.assertEqual(getDateOnRightFormat(month[n]),correcktMonth[n])
    def test_isNumber(self):
        inList= ["1","s","+","@",",","3"]
        correctList=[True,False,False,False,False,True]
        for n in range(len(inList)):
            self.assertEqual(isNumber(inList[n]),correctList[n])

    def test_prepDeliveriesForDatabase_sample_scrape_correct(self):
        scrapeList =[['Assignment 2', 'TDT4300 DATAVAREH/DATAGRUVED V\xc5R 2017', 'Deadline: 10. mars 2017 08:00'], ['Assignment 2: Demonstrated learning of Core 1', 'TDT4140 PROGRAMVAREUTVIKL V\xc5R 2017', 'Deadline: 10. mars 2017 23:55'],['fsvsdv', 'zxce', 'D12fv']]
        correctList = [[' Assignment 2', ' TDT4300 DATAVAREH/DATAGRUVED', '2017-03-10', '08:00:00'], [' Assignment 2:', ' TDT4140 PROGRAMVAREUTVIKL', '2017-03-10', '23:55:00'],['', '', '00-00-00', '00:00:00']]
        for n in range(len(scrapeList)):
            self.assertEqual(prepDeliveriesForDatabase(scrapeList[n]),correctList[n])

    def test_prepAllDeiveriesForDatabase_sample_scrape_correct(self):
        scrapeList =[['Assignment 2', 'TDT4300 DATAVAREH/DATAGRUVED V\xc5R 2017', 'Deadline: 10. mars 2017 08:00'], ['Assignment 2: Demonstrated learning of Core 1', 'TDT4140 PROGRAMVAREUTVIKL V\xc5R 2017', 'Deadline: 10. mars 2017 23:55'],['fsvsdv', 'zxce', 'D12fv']]
        correctList = [[' Assignment 2', ' TDT4300 DATAVAREH/DATAGRUVED', '2017-03-10', '08:00:00'], [' Assignment 2:', ' TDT4140 PROGRAMVAREUTVIKL', '2017-03-10', '23:55:00'],['', '', '00-00-00', '00:00:00']]
        self.assertEqual(prepAllDeiveriesForDatabase(scrapeList),correctList)
    # def test_getUsername(self):
    #     correctUname="eirikriv"
    #     username = getUsername()
    #     self.assertEqual(username,correctUname)
    # def test_getUsername(self):
    #     correctPass="12345"
    #     password = getUserPassword()
    #     self.assertEqual(password,correctPass)


if __name__ == '__main__':
    unittest.main()