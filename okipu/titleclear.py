# -*- coding: utf8 -*-
import pyodbc
import datetime
import re
import requests
from bs4 import  BeautifulSoup
#import numpy as np

def TrConvert(text):
        convert = {
                "ü":"u",
                "Ü":"U",
                "ö":"o",
                "Ö":"O",
                "ç":"c",
                "Ç":"C",
                "ş":"s",
                "Ş":"s",
                "ğ":"g",
                "Ğ":"G",
                "İ":"I",
                "ı":"i",
                " ":"-"
        }
        for karakter in convert:
                if karakter in text:
                        text =  text.replace(karakter, convert[karakter])
        return text.lower()

mainurl ="https://www.kitapyurdu.com/"
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows con string
cursor = conn.cursor()
cursor.execute("select Id,Title,Isbn,Comment from BOOKS order by Id DESC")
books = cursor.fetchall()

for b in books:
    title = b[1]
    isbn = b[2]
    comment = b[3]
    if comment.find("Kitap Özellikleri") > -1 or comment.find("Açıklaması ve Özellikleri") > -1:
        converted = TrConvert(title)
        print(isbn + " " + title +" -- "+ converted)

response = requests.get(mainurl+converted)
html_content = response.content
soup = BeautifulSoup(html_content.decode('utf-8', 'ignore'),"html.parser")
hrefs = soup.find_all("div",{"class":"cover"})