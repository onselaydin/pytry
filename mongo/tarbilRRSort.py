from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
sale = mydb["tarbilRr"]
total = sale.find().sort({"time":-1}).limit(100)
for x in total:
    print(x)