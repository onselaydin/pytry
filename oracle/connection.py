import cx_Oracle
##import pyodbc
#tns = cx_Oracle.makedsn('alsrac-scan.alisannak.com', '1521', service_name='local')     
#con = cx_Oracle.connect('LOS','LO1907','alsrac-scan.alisannak.com/local',encoding="UTF-8")
con = cx_Oracle.connect('LOS/LO1907@alsrac-scan.alisannak.com:1521/local') 
#con = pyodbc.connect('DRIVER={oracledriver};SERVER=alsrac-scan.alisannak.com;DATABASE=LOS;UID=LOS;PWD=LO1907')
cursor = con.cursor() 
cursor.arraysize=50    
cursor.execute("SELECT * FROM LOS.CARIAGRO_CN where ROWNUM <= 100")
rows = cursor.fetchall()
for result in rows:
    print(result)                    
print("successful") 
      