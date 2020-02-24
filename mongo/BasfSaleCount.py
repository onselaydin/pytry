from pymongo import MongoClient
from datetime import datetime
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
sale = mydb["sale"]
documentno='816282'
#start = datetime(2020, 1, 30)

saletotal = sale.count_documents({"document.no":documentno})
#saletotal = sale.find({"$or":[{"document.no":"3535001990"},{"notifiyTime":start}]})

print(saletotal)