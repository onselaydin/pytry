import csv
import datetime
import pyodbc
from decimal import Decimal

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
cursor = conn.cursor()
cursor.execute("""select b.Id,b.Title,w.Name as Writer, b.Translator, p.Name as Publisher, b.Comment,b.Language,
b.Isbn, b.BookEdition, b.NumberofPages, b.HardcoverType, b.PaperType, b.ProductDimensions,
bc.CategoryName, b.IsActive, b.Company, b.Update_Date from BOOKS b, WRITERS w, BOOK_CATEGORIES bc,PUBLISHERS p
where
w.Id = b.Writer and
bc.Id = b.BookCategory and
p.Id = b.Publisher""")
books = cursor.fetchall()


with open("output.csv", "w", encoding='utf-8') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in books:
        print(row[1])
        writer.writerow(row)

cursor.close()
conn.close()