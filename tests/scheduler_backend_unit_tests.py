import sys

#sys.path.append("../src/scraper")
#sys.path.append("../src/databasehandler")
sys.path.append("../src/scheduler")
#from insertionMethods import *
#from massageItslearningData import *	
#from readItslearningAssignments import *
#from scrapeForCoursesItslearning import *
#from clearDBConnect import *
import unittest
from scheduler import ofsetDateByANumberOfDays

class massageItslearningDataTester(unittest.TestCase):
    # def test_monthConverter_all_months_correct_number(self):
    #     months=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
    #     counter = 1
    #     for month in months:
    #         self.assertEqual(monthConverter(month), str(counter))
    #         counter +=1

    # def test_monthConverter_wrong_month_format_error_flag(self):
    #     incorretcMonths=["jan", "feb" ,"January","Janu"]
    #     for incorretcMonth in incorretcMonths:
    #         self.assertEqual(monthConverter(incorretcMonth),"00")
    
    # def test_getDateOnRightFormat_sample_days_correct(self): 
    #     days = ["01","31","15",".7",".3","12.","03"]
    #     correctDays=["01","31","15","07","03","12","03"]
    # 	for n in range(len(days)-1):
    # 		self.assertEqual(getDateOnRightFormat(days[n]),correctDays[n])

    # def test_getDateOnRightFormat_sample_days_incorrect_flagg(self):
    # 	month = ["0112","3121","1415",".417",".13f",1,"abba","02","12"]
    # 	correcktMonth=["00","00","00","00","00","00","00","02","12"]
    # 	for n in range(len(month)-1):
    # 		self.assertEqual(getDateOnRightFormat(month[n]),correcktMonth[n])
    # def test_isNumber(self):
    #     inList= ["1","s","+","@",",","3"]
    #     correctList=[True,False,False,False,False,True]
    #     for n in range(len(inList)):
    #        self.assertEqual(isNumber(inList[n]),correctList[n])
    def test_ofsetDateByANumberOfDays(self):
        dates = ["20190204",3,"20170314",-3,"20170314",1,"20170314",-14,"20170314",19]
        correct_dates = ["2019-02-07","2017-03-11","2017-03-15","2017-02-28","2017-04-02"]
        self.assertEqual(ofsetDateByANumberOfDays("2017-03-14",-3),"2017-03-11")


if __name__ == '__main__':
    unittest.main()