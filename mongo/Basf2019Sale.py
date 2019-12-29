from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
glnno = "8681957313010"

sale = mydb["sale"]
singlesale = mydb["single_sale"]

saletotal = sale.count_documents({"from.gln":glnno})
singlesaletotal = singlesale.count_documents({"from.gln":glnno})

print(saletotal + singlesaletotal)

# %%
#section 1
print('diyez boşluk  ve iki yüzde yan yana section 1 çalıştı')

# %%
print('section 2 çalıştı')

# %%


# %%
