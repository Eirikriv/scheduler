# Start up an Xvfb display that has 0 window size
from pyvirtualdisplay import Display
#display.sendstop() #use this to close display after running 
# Load a Firefox selenium webdriver session
from selenium import webdriver
from getpass import getpass

import time
#import time to slow selenium down



def startdisplay():
    display = Display(visible=0, size=(800, 600))
    display.start()

def closedisplay():
    display.sendstop() 


def scrapeItslearning():
    driver = webdriver.Firefox()
    u_username=input("NTNU username: ")
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

    time.sleep(2)

    driver.get('https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx')

    driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

    courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

    singleReturnVar = ""

    for course in courses:
        singleReturnVar = course.text
        break

    browser.close()

    return singleReturnVar
startdisplay()
print(scrapeItslearning())
closedisplay()
