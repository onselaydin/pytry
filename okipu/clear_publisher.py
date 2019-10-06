import pyodbc
import clearmod
#driver = '/usr/local/lib/libtdsodbc.so'
#dbcinst -j
#https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
cursor = conn.cursor()
try:
    
    cursor.execute("select Id, Publisher from BOOKS")
    books = cursor.fetchall()
#for i in books:
#    print(i)

    for book in books:
        id = book[0]
        a = clearmod.clear(book[1])

        cursor.execute("update BOOKS set Publisher=? where Id=?", a, id)      
        conn.commit()
        print(book[1] +"  book cleared")
    print("process finished.")
except pyodbc.Error as ex:
    conn.rollback()
    print("error "+ ex.args[0])
conn.close()