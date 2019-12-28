from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['AGRO']
sale = mydb["sale"]
total = sale.find({"document.no":"007234"},{"state":"done"}).count()
print(total)