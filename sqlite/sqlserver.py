import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}')
cursor = conn.cursor()
cursor.execute("select top 50 * from ENTLOG order by UPDATE_DATE DESC")
sonuc = cursor.fetchall()
for i in sonuc:
    print(i)
conn.close()