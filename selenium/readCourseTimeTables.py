from pyvirtualdisplay import Display
from selenium import webdriver
import time

def startdisplay():
    display = Display(visible=0, size=(800, 600))
    display.start()

def scrapeNtnuCourseWebsites(courseCode): #eks TIO4110, gives a long string of courses and times, needs to be modified
    driver = webdriver.Firefox()
    webpage = "https://www.ntnu.no/studier/emner/"+courseCode+"#tab=timeplan"
    driver.get(webpage)
    time.sleep(1)
    courseTable=driver.find_element_by_class_name("wrap")
    driver.close()
    return courseTable.text

startdisplay()
coursename=scrapeNtnuCourseWebsites("TDT4140")
print(coursename)
