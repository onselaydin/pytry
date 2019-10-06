import pyodbc
import datetime
import re
try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
    cursor = conn.cursor()
    cursor.execute("select Id, Publisher from BOOKS order by Id DESC")
    books = cursor.fetchall()

    for book in books:
        id = book[0]
        pub = book[1]
        print(str(pub.strip())+" bakılıyor")

        cursor.execute("SELECT distinct Id, Name FROM PUBLISHERS WHERE Name=?",(pub))
        fpublishers = cursor.fetchall()
        cpublishers = re.findall("[A-Za-z]", pub)

        if len(fpublishers) == 0 and len(cpublishers) > 0:
            now = datetime.datetime.now()
            cursor.execute("INSERT INTO PUBLISHERS (Name, Update_Date) values (?,?)", (pub,now))
            conn.commit()

            cursor.execute("SELECT distinct Id, Name FROM PUBLISHERS WHERE Name=?",(pub))
            fpub = cursor.fetchall()
            for row in fpub:
                r = row[0]
                cursor.execute("update BOOKS set Publisher=? where Id=?", r, id)
                conn.commit()
        elif len(fpublishers) > 0:
            cursor.execute("SELECT distinct Id, Name FROM PUBLISHERS WHERE Name=?",(pub))
            ppub = cursor.fetchall()
            for prow in ppub:
                p = prow[0]
                cursor.execute("update BOOKS set Publisher=? where Id=?", p, id)
                conn.commit()
    print(pub+" saved")
    conn.close()        

except pyodbc.Error as ex:
    print(pub + " error "+ ex.args[0])