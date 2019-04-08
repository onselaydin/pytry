import pyodbc
import datetime
import re
import requests
from bs4 import  BeautifulSoup
#import numpy as np

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
cursor = conn.cursor()
cursor.execute("select Id,Title,Comment from BOOKS order by Id DESC")
books = cursor.fetchall()

for b in books:
    title = b[1]
    book = b[2]
    if book.find("Kitap Özellikleri") > -1 or book.find("Açıklaması ve Özellikleri") > -1:
        print(title + " " + book)

