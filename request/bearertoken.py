import requests
import json

#token al
turl = 'http://bkst.tarbil.gov.tr/Service/Token'
tdata = {"grant_type" : "password", 
"username":"20110402044",
"password":"20155044",
"Content-Type":"application/x-www-form-urlencoded" }
tresponse = requests.post(turl, tdata)
token = tresponse.json()['access_token']

#satış
hed = {"Authorization": "Bearer " + token}
data = {
    "Gln":"8696851000034",
    "Key":"e2a710fa-7ec7-4836-b6e5-f57310a6dc80",
    "DocumentHeader": {
            "sender": "8696851000034",
            "receiver": "0632001800015",
            "key": "e2a710fa-7ec7-4836-b6e5-f57310a6dc80",
            "actionType": "S",
            "documentNumber": "858104824",
            "documentDate": "2020-02-19",
            "note": "Satış Bildirimi",
            "deactivationNote": "",
            "exportReceiverNote": "",
            "exportCountry": None,
            "importSenderNote": "",
            "importCountry": None,
            "returnNote": "",
            "destructionNote": "",
            "idTaxNo": ""
        },
    "DocumentDetail":[{
                "serialNumber": "904690120136383",
                "lotNumber": "F469J17005",
                "gtinNumber": "03362130039259",
                "parentCarrierNo": "",
                "carrierNo": "",
                "productNote": "test",
                "productionDate": "05.01.2019",
                "expirationDate": "05.01.2021" 
                }],
    "Content-Type":"application/x-www-form-urlencoded"
}
res = requests.put('http://bkst.tarbil.gov.tr/Service/api/main/setTransactionAndDetail',data,headers=hed)
print(res.json())