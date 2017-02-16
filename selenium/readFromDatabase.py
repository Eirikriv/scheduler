from database import db
from database import Courses

def getLastentryfromDatabase():
    courses = Courses.query.all()
    returnVar = ""
    for course in courses:
        returnVar = course.coursename
    return returnVar

print(getLastentryfromDatabase())
