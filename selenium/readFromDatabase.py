from database import db
from database import Courses

#returns the last entry in the "Courses" database

def getLastentryfromDatabase():
    courses = Courses.query.all()
    returnVar = ""
    for course in courses:
        returnVar = course.coursename
    return returnVar

#printfunction can be removed, this is jus to test
print(getLastentryfromDatabase())
