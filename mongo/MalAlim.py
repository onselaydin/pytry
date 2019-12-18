from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['AGRO']
receive = mydb["receive"]
total = receive.find({"document.no":"278337","product.gtin.no":"08697837195249","to.gln":"8697837190015"})
for x in total:
    print(x)