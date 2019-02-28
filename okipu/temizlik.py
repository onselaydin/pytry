import pyodbc
import clearmod
#driver = '/usr/local/lib/libtdsodbc.so'
#dbcinst -j
#https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017

try:
    #conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
    cursor = conn.cursor()
    cursor.execute("select Id, Title, Writer, Translator, Isbn, Comment from BOOKS")
    books = cursor.fetchall()
#for i in books:
#    print(i)

    for book in books:
        id = book[0]
        a = clearmod.clear(book[1])
        b = clearmod.clear(book[2])
        c = clearmod.clear(book[3])
        d = clearmod.clear(book[4])
        e = clearmod.clear(book[5])
        cursor.execute("update BOOKS set Title=?,Writer=?,Translator=?,Isbn=?,Comment=? where Id=?", a,b,c,d,e,id)      
        print(book[1] +"  kitabı temizlendi...")
    print("işlem tamamlandı")
except pyodbc.Error as ex:
    conn.rollback()
    print("Bir hata oluştu "+ ex.args[0])
conn.commit()
conn.close()