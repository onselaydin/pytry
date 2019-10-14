from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
cus = mydb["single_receive"]
agr = [{'$group': {'_id':"$from.gln" }}]
val = list(cus.aggregate(agr))
for gln in val:
    print(gln['_id'])