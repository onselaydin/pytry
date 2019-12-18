from pymongo import MongoClient
client = MongoClient('10.16.15.89', 27017)
client.admin.authenticate('agros', 'agros1234', mechanism = 'SCRAM-SHA-1', source='agros')
mydb = client['LOS']
glnno = "0632003030007"

deactive = mydb["deactive"]
imports = mydb["import"]
receive = mydb["receive"]
salecancel = mydb["saleCancel"]
singledeactive = mydb["single_deactive"]
singleimport = mydb["single_import"]
singlereceive = mydb["single_receive"]
singlesale = mydb["single_sale"]
singlesalecancel = mydb["single_saleCancel"]

deactivetotal = deactive.count_documents({"to.gln":glnno})
importstotal = imports.count_documents({"to.gln":glnno})
receivetotal = receive.count_documents({"to.gln":glnno})
salecanceltotal = salecancel.count_documents({"to.gln":glnno})
singledeactivetotal = singledeactive.count_documents({"to.gln":glnno})
singleimporttotal = singleimport.count_documents({"to.gln":glnno})
singlereceivetotal = singlereceive.count_documents({"to.gln":glnno})
singlesaletotal = singlesale.count_documents({"to.gln":glnno})
singlesalecanceltotal = singlesalecancel.count_documents({"to.gln":glnno})

print(deactivetotal + importstotal + receivetotal + salecanceltotal + singledeactivetotal + singleimporttotal + singlereceivetotal + singlesaletotal + singlesalecanceltotal)