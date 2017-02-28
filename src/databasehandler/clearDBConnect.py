from sqlalchemy import create_engine
import os
from database2 import *
username = unameHeroku
password = passwordHeroku


URI = 'mysql://'+str(username)+':'+str(password)+'@us-cdbr-iron-east-04.cleardb.net/heroku_f8b7f102c73b268'
db = create_engine(URI)
print(db.table_names())

