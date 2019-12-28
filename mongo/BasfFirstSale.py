from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
glnno = "8681957313010"

sale = mydb["sale"]

saletotal = sale.find_one({"from.gln":glnno}) #.sort({"createdTime", -1})

print(saletotal)