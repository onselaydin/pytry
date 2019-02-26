import pyodbc
import clearmod

'''
b = clearmod.clear("Sakarya &Uuml;niversitesi Mekatronik Mühendisliği")
print (b)
'''

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}')
cursor = conn.cursor()



cursor.execute("select top 10 Title, Writer, Translator, Isbn, Comment from BOOKS")
books = cursor.fetchall()

for book in books:
    a = clearmod.clear(book[0])
    print(a)
    '''
    b = clearmod.clear(book[1])
    print(b)
    c = clearmod.clear(book[2])
    print(c)
    '''
#for i,j in donustur.items():
#    print(i,j)
