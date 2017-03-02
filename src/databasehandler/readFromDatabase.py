from database import db
from database import Courses
import json
#returns the last entry in the "Courses" database

def getLastEntryFromDatabase():
    courses = Courses.query.all()
    returnList = []
    for course in courses:
        returnList.append(course.studentID)
        returnList.append(course.courseName)
        returnList.append(course.startTime)
        returnList.append(course.endTime)
        returnList.append(course.stardate)
        returnList.append(course.enddate)
        returnList.append(course.description)    
        returnList.append(course.location)
        returnList.append(course.attachments)
	break
    return returnList

#printfunction can be removed, this is jus to test

def createJson(studentID, courseName, startTime, endTime, stardate, enddate, description, location, attachment):
    data = {"studentID": studentID, "courseName": courseName, "startTime" : startTime, "endTime" : endTime, "startdate":stardate, "enddate":enddate, "description":description ,"location" : location, "attachment": attachment}
    json_data = json.dumps(data)
    return json_data

def createAndReturnJson():
    courseList=[]
    courseList=getLastentryfromDatabase()
    json_data = createJson(courseList[0], courseList[1], courseList[2], courseList[3], courseList[4], courseList[5], courseList[6], courseList[7], courseList[8])
    return json_data
print(createAndReturnJson())
    

    
