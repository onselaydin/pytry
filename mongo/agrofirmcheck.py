from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['AGRO']
sale = mydb["sale"]
total = sale.find({"from.gln":{"$regex":"^0341029860009"}}).limit(1).sort("notifiyTime",-1)
for x in total:
    print(x)