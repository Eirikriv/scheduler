import sys
sys.path.append("../scraper")
from insertionMethods import *
from scrapeForCoursesItslearning import *
import traceback
from databaseConnectDetails import *

def controllScannForLecturesandInsert(courseCode):
	lectures , courseCode = scrapeNtnuCourseWebsites("TDT4140")
	lectureTimes = readCourseReturnAllLectureExersiseEvents(lectures, courseCode, "2017")
	counter = 0
	errorCounter = 0
	engine = create_engine(URI)
	connection = engine.connect()
	if(getValueFromCourseTable(engine, connection, courseCode)):
		insertCourseIntoDatabase(courseCode, courseCode)
	for types in lectureTimes:
		for events in types:
			try: 
				lastEntry = getLastEntryFromLectureTable(engine, connection)
				lectureID = lastEntry[0]
				lectureID = str(int(lectureID)+1)
				lectureID = (6-len(lectureID))*"0" + lectureID
			except:
				lectureID = "000001"
			date = events[1].split("T")[0]
			start = events[1].split("T")[1]
			end = events[2].split("T")[1]
			description = events[3]
			where=events[4]
			if(insertLectureIntoDatabase(engine,connection,lectureID,date,start,end,description,where)):
				counter += 1
				insertLectureCourseIntoDatabase(engine,connection,lectureID,courseCode)
			else:
				errorCounter += 1 
	print "successfully inserted: " + str(counter) + " of: " + str(errorCounter+counter) +  " entries" 

controllScannForLecturesandInsert("TDT4140")
