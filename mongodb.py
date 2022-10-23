from typing import Any, Mapping

import pymongo
from pymongo import MongoClient
from pymongo.database import Database
#create mongodb client, cluster
client = MongoClient("mongodb+srv://kocsog:b587331B@cluster0.uwoii6q.mongodb.net/?retryWrites=true&w=majority")

# (mongodb+srv://patrik1003:<password>@cluster0.q68jswv.mongodb.net/?retryWrites=true&w=majority)

# this is my created localhost
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')

#new database
mydb = client['mydatabase']

# this list the names of the database
# print(myclient.list_database_names())

# it is controlling the names of the database
# dblist = myclient.list_database_names()
# if "admin" in dblist:
#    print("The database exists")