import pyodbc
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
    cursor = conn.cursor()
    cursor.execute("select Id, Title, Writer, Translator, Isbn, Comment from BOOKS")
    books = cursor.fetchall()
    for book in books:
        id = book[0]
        a = book[1].strip()
        b = book[2].strip()
        c = book[3].strip()
        d = book[4].strip()
        e = book[5].strip()
        cursor.execute("update BOOKS set Title=?,Writer=?,Translator=?,Isbn=?,Comment=? where Id=?", a, b, c, d, e, id)      
        print(book[1] +"  temizlendi...")
    print("islem tamamlandi")
except pyodbc.Error as ex:
    conn.rollback()
    print("Bir hata olustu "+ ex.args[0])
conn.commit()
conn.close()