from pymongo import MongoClient
from datetime import datetime
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
sale = mydb["sale"]

saletotal = sale.count_documents({"channel":{"$eq" : None}})
#saletotal = sale.find({"$or":[{"document.no":"3535001990"},{"notifiyTime":start}]})

print(saletotal)