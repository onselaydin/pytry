from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['AGRO']
sale = mydb["sale"]
#total = sale.find({"document.no":"278337"}) #.sort('createdTime', -1).limit(1)[0]
for x in sale.find({"document.no":"278337"}):
    print(x)