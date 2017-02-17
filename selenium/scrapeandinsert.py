# Start up an Xvfb display that has 0 window size
from pyvirtualdisplay import Display
#display.sendstop() #use this to close display after running 
# Load a Firefox selenium webdriver session
from selenium import webdriver
from getpass import getpass
from database import db
from database import Courses
from createEvent import create_event
import time
#import time to slow selenium down

#inserts a row into the Courses database
def insertIntoDatabase(studentid, courseid, coursename):
    insertion = Courses(studentid,courseid,coursename)
    db.session.add(insertion)
    db.session.commit()


#Starts a virtual display, needed to run selenium on linux server
def startdisplay():
    display = Display(visible=0, size=(800, 600))
    display.start()

#Asks for username and password in console, then scrapes the itslearning page for the given username
#Returns the last course in the "Active" courselist
def scrapeItslearning():
    driver = webdriver.Firefox()
    u_username=raw_input("NTNU username: ")
    u_password=getpass("NTNU password: ") 
    driver.get('http://www.instabart.no/') 

    pressend=driver.find_element_by_class_name("itslearning")
    time.sleep(1)
    pressend.click()

    time.sleep(3)
    its=driver.find_element_by_id("username")
    time.sleep(1)
    its.send_keys(u_username) 

    passwd = driver.find_element_by_id("password")
    time.sleep(1)
    passwd.send_keys(u_password)


    loginbutton = driver.find_element_by_class_name("submit")
    time.sleep(1)
    loginbutton.click()

    time.sleep(4)

    driver.get('https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx')
    time.sleep(4)
    driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
    time.sleep(4)
    courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

    singleReturnVar = ""

    for course in courses:
        singleReturnVar = course.text
        break

    driver.close()
    return singleReturnVar

#Scrapes, then inserts course into database with stuentid and courseid as hard-coded constants

def main():
    startdisplay()
    coursename=scrapeItslearning()
    print(coursename)
    insertIntoDatabase("01","01",coursename)
    time.sleep(8)
    create_event("23.02.2017")
main()
