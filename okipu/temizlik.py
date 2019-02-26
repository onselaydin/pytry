import pyodbc
import clearmod
driver = '/usr/local/lib/libtdsodbc.so'
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}')
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}')
cursor = conn.cursor()
cursor.execute("select top 10 Id, Title, Writer, Translator, Isbn, Comment from BOOKS")
books = cursor.fetchall()


for i in books:
    print(i)

conn.close()