import time

#Converts to the form: [AssimentDetails, CourseName, deadline date, deadline time]

def monthConverter(monthAsString):
    months=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
    returnVar = 0
    for n in range(len(months)):
        if months[n]==monthAsString:
            returnVar = n + 1 
            break
    if(returnVar==0):
        returnVar = "00" 
    return returnVar

    
def getDayOnRightFormat(day): 
    
    returnVar = 0 
    
    try:
        len(day)
        if(len(day) <=1 or len(day) >= 3):
            returnVar = "00"
        else:
            if(day[0]=="."):
                returnVar = "0" + day[1]
            else:
                returnVar = day
    except: 
        return "00"
    
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