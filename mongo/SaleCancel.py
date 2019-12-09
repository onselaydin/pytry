from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
salecancel = mydb["saleCancel"]
singlesale = mydb["single_saleCancel"]
total = salecancel.find().count() + singlesale.find().count()
print(total)