import cx_Oracle
import requests
import json
import glnquery

# con = cx_Oracle.connect('LOS/LO1907@alsrac-scan.alisannak.com:1521/local') 
# cursor = con.cursor() 
# cursor.arraysize=50    
# cursor.execute("SELECT * FROM LOS.CARIAGRO_C where ROWNUM <= 100")
# rows = cursor.fetchall()
# for result in rows:
#     print(result)                    
# print("successful") 

# cursor.execute("update BOOKS set Writer=? where Id=?", wid, id)
#                 conn.commit()

#token aldık
# turl = 'http://bkst.tarbil.gov.tr/Service/Token'
# tdata = {"grant_type" : "password", 
# "username":"20110402044",
# "password":"20155044",
# "Content-Type":"application/x-www-form-urlencoded" }
# tresponse = requests.post(turl, tdata)
# token = tresponse.json()['access_token']

#karekod sorgulama
#product/qrcode?Gln=2011040204402&Key=f35f0ce2-345d-4c5e-b1ed-6997c32b48e4&Gtin=00000000000027
gln='8696851000034'
gtin='03362130039259'
key = 'e2a710fa-7ec7-4836-b6e5-f57310a6dc80',
purl = 'http://10.16.15.140/tarbil.api/product/qrcode?Gln='+gln+'&Key='+key[0]+'&Gtin='+gtin+''

presponse = requests.get(purl)
print(presponse.json())
