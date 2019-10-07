##import pymongo
#https://www.w3schools.com/python/python_mongodb_update.asp
from pymongo import MongoClient
#import numpy as np
#import urllib

client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['AGRO']
cus = mydb["customer"]
#query = { "name": { "$gt": "S" } }
#query = { "name": "Gökhan Tarım İlaçları A.Ş"}
#query = { "name": { "$regex": "^S" } }
customers = mydb["customer"]

#for cus in customers.find(query):
for cus in customers.find().sort("name", -1):
  print(cus['name'] + ' - ' + cus['firmCode'])