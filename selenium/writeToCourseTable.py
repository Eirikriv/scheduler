from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('https://www.ntnu.no/studier/emner/TDT4140#tab=timeplan')
time.sleep(1)
courseTable=driver.find_element_by_class_name("wrap")

text= courseTable.text

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
unicode_string = text.encode('utf-8')
text_file = open("courseContent.txt","w")
text_file.write(unicode_string)
text_file.close()
