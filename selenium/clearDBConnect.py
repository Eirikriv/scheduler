from sqlalchemy import create_engine

db = create_engine('mysql://"edited":"edited"@us-cdbr-iron-east-04.cleardb.net/heroku_f8b7f102c73b268')


print(db.table_names())

