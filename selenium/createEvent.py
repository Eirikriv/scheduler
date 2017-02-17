from __future__ import print_function
import httplib2
import os
import sys
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime
from database import db
from database import Courses

#returns the last entry in the "Courses" database
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')
    print("I run!")
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getLastentryfromDatabase():
    courses = Courses.query.all()
    returnVar = ""
    for course in courses:
        returnVar = course.coursename
    return returnVar

def formatAndChangeStartDate(dato):

  today = datetime.datetime(int(dato[6:11]), int(dato[3:5]) , int(dato[0:2]), 18, 00)
  DD = datetime.timedelta(days=5)
  earlier = today - DD
  earlier_str = earlier.strftime("%Y%m%d")
  return earlier_str

def create_event(tittel, dato):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    date = formatAndChangeStartDate(dato)
    service = discovery.build('calendar', 'v3', http=http)
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    tittel = getLastentryfromDatabase()   
    event = {
      'summary': 'paamelding til '+tittel,
      'location': 'Kjel',
      'description': tittel,
      'start': {
        'dateTime': date[0:4]+'-'+date[4:6]+'-'+date[6:8]+'T11:57:00',
        'timeZone': 'Europe/Oslo',
      },
      'end': {
        'dateTime': date[0:4]+'-'+date[4:6]+'-'+date[6:8]+'T12:00:00',
        'timeZone': 'Europe/Oslo',
      },
      'reminders': {
        'useDefault': True,
      },
    }
    print(event)
    event = service.events().insert(calendarId='primary', body=event).execute()

create_event("Pause","22.02.2017")
