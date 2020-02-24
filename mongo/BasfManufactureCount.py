from pymongo import MongoClient
from datetime import datetime
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
collection = mydb["manufacture"]

manufacturetotal = collection.count_documents({"from.firmCode":"2112"})

print(manufacturetotal)