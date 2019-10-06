import pyodbc
import datetime
import re
try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}')
    cursor = conn.cursor()
    cursor.execute("select * from BOOK_CATEGORIES where Id NOT IN (1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,46,55,95,97,98,99,102,142,159)")
    books = cursor.fetchall()

    for book in books:
        bk = book[0]
        print(bk)
        cursor.execute("delete from BOOK_CATEGORIES where Id=?", bk)
        conn.commit()
except pyodbc.Error as ex:
    print(" error "+ ex.args[0])