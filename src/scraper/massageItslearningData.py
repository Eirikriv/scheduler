import time

#Converts to the form: [AssimentDetails, CourseName, deadline date, deadline time]

def mounthConverter(mounthAsString):
    mounths=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
    returnVar = 0
    for n in range(len(mounths)):
        if mounths[n]==mounthAsString:
            returnVar = n + 1 
            break
    if(returnVar==0):
        returnVar = "00" #returns 00 if name of mounth is not found 
    return returnVar

    
def getDayOnRightFormat(day): #Handles cases where days can be 3. or 12. then adds a 0 in front of 3. and removes .
    returnVar = 0
    if(len(day) <=1):
        returnVar = "00"
    else:
        returnday = day[0:-1]
        print returnday
        if len(returnday)>=2:     #returns 00 if the day is not between 1 and 31
            returnVar = returnday
        else:
            returnVar = "0"+returnday
    return returnVar

def getMounthOnRightFormat(mounth):
    returnVar=0
    if(mounth=="00"):
        returnVar = "00"
    else:
        if len(mounth)>=2:
            returnVar = mounth
        else:
            returnVar = "0"+mounth
    return returnVar

def prepDeliveriesForDatabase(rawScrapeFromIts): #converts to applicable databaeformat, returns on formate:
    returnList=[]                                #[assingmentdetails, coursename, date, time]
    assigmentDetailsSting = rawScrapeFromIts[0]
    assigmnentDetails = assigmentDetailsSting.split()
    crDetails = ""
    for n in range(0,len(assigmnentDetails)):
        crDetails=crDetails+" "+assigmnentDetails[n]
        if n == 1:
            break
    returnList.append(crDetails)

    courseNameString = rawScrapeFromIts[1]
    courseName = courseNameString.split()
    name = courseName[0:len(courseName)-2]
    crName=""
    for words in name:
        crName = crName + " "+ words 
    returnList.append(crName)

    deadLineDetailsString = rawScrapeFromIts[2]
    deadLineDetails = deadLineDetailsString.split()
    day = getDayOnRightFormat(deadLineDetails[1])
    mounth=mounthConverter(deadLineDetails[2])
    mounth=getMounthOnRightFormat(mounth)

    year = deadLineDetails[3]
    dateString = year + "-" + mounth + "-" + day
    returnList.append(dateString)

    time = deadLineDetails[4]
    time = time + ":00"

    returnList.append(time)
    return returnList


def prepAllDeiveriesForDatabase(totalDeliveryList): #prepares for all assingments found on itslearning
    returnList = []
    for deliveries in totalDeliveryList:
        returnList.append(prepDeliveriesForDatabase(deliveries))
    return returnList

def massageItsLearningDataMain():
    rawList = scrapeItslearning()
    readyForDataBase = prepAllDeiveriesForDatabase(rawList)
    return readyForDataBase