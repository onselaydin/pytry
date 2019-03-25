import pyodbc
import datetime
import re

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
cursor = conn.cursor()
w = "Али Мертхан Дюндар"
cursor.execute("select Id, Writer from BOOKS where Writer=?",(w))
books = cursor.fetchall()

for book in books:
    id = book[0]
    writer = book[1]

print(id)