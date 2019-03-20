import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
    cursor = conn.cursor()
    cursor.execute("select Id, Writer from BOOKS")
    books = cursor.fetchall()

    for book in books:
        id = book[0]
        writer = book[1]
        cursor.execute("SELECT distinct Id, Name FROM WRITERS WHERE Name=?",(writer))
        fwriters = cursor.fetchall()
        if len(fwriters) > 0:
            for fwriter in fwriters:
                wid = fwriter[0]
                cursor.execute("update BOOKS set Writer=? where Id=?", wid, id)
                print(writer + " güncellendi")
    print("All writers updated...")
except pyodbc.Error as ex:
    conn.rollback()
    print("Bir hata oluştu "+ ex.args[0])
conn.commit()
conn.close()