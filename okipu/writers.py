import pyodbc
import datetime
import re
try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
    cursor = conn.cursor()
    cursor.execute("select Id, Writer from BOOKS order by Id DESC")
    books = cursor.fetchall()

    for book in books:
        id = book[0]
        writer = book[1]
        print(str(id)+" bakılıyor")
        if writer.find(",") > -1:
            writer = writer.split(",")
            writer = writer[0].strip()

        cursor.execute("SELECT distinct Id, Name FROM WRITERS WHERE Name=?",(writer))
        fwriters = cursor.fetchall()
        cwriter = re.findall("[A-Za-z]", writer)
            
        if len(cwriter) > 0:
            for fwriter in fwriters:
                wid = fwriter[0]
                cursor.execute("update BOOKS set Writer=? where Id=?", wid, id)
                conn.commit()
                print(writer + " güncellendi")
        elif len(cwriter) == 0 and len(cwriter) > 0:
            now = datetime.datetime.now()
            cursor.execute("INSERT INTO WRITERS (Name, Update_Date) values (?,?)", (writer,now))
            conn.commit()
            print(writer+" saved")
    conn.close()        
except pyodbc.Error as ex:
#    conn.rollback()
    print(writer + " error "+ ex.args[0])
