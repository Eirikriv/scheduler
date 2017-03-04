from sqlalchemy import create_engine, MetaData,Table, select
import os
#from databaseConnectDetails import *


#username = unameHeroku
#password = passwordHeroku
#URI = 'mysql://'+str(username)+':'+str(password)+'@us-cdbr-iron-east-04.cleardb.net/heroku_f8b7f102c73b268'


def insertUserIntoDatabase(StringUserID,StringUserName):
	engine = create_engine(URI)
	connection = engine.connect()
	metadata = MetaData()
	user = Table('user', metadata, autoload=True , autoload_with=engine)
	ins = user.insert()
	new_user = ins.values(userID=StringUserID,userName=StringUserName)
	connection.execute(new_user)	
#insertUserIntoDatabase("0004","Eirik Rivedal")

def getEntryFromUserTable(stringUserId):
	engine = create_engine(URI)
	connection = engine.connect()
	metadata = MetaData()
	user = Table('user', metadata, autoload=True , autoload_with=engine)
	selectUser = select([user]).where(user.c.userID == stringUserId)
	for row in connection.execute(selectUser):
		return row

getEntryFromUserTable("0004")


#print(engine.table_names())












#print(repr(user))

#stmt = 'SELECT * FROM user'
#result_proxy = connection.execute(stmt)
#results = result_proxy.fetchall()
#print results
# firstRow = results[0]
# firstRowKeys = firstRow.keys()



