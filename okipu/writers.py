import pyodbc
import datetime
import re
try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
    cursor = conn.cursor()
    cursor.execute("select Id, Writer from BOOKS")
    books = cursor.fetchall()

    for book in books:
        id = book[0]
        writer = book[1]
        if writer.find(",") > -1:
            writer = writer.split(",")
            writer = writer[0].strip()

        cursor.execute("SELECT distinct Id, Name FROM WRITERS WHERE Name=?",(writer))
        fwriters = cursor.fetchall()
        cwriter = re.findall("[A-Za-z]", writer)
            
        if len(fwriters) > 0:
            for fwriter in fwriters:
                wid = fwriter[0]
                cursor.execute("update BOOKS set Writer=? where Id=?", wid, id)
                print(writer + " güncellendi")
        elif len(fwriters) == 0 and len(cwriter) > 0:
            now = datetime.datetime.now()
            cursor.execute("INSERT INTO WRITERS (Name, Update_Date) values (?,?)", (writer,now))
            print(writer+" saved")
except pyodbc.Error as ex:
    conn.rollback()
    print(writer + "da bir hata oluştu "+ ex.args[0])
conn.commit()
conn.close()