import requests
from bs4 import  BeautifulSoup
import datetime
from time import sleep
import pyodbc
import urllib.request
import os
import glob
import ftplib
import re #regex kutuphanesi

def GetNewBookLinks():
    #https://canyayinlari.com/kitaplar/?SayfaNo=1
    #url = "https://www.kitapyurdu.com/index.php?route=product/category&path=128_159&filter_in_stock=1&page="+str(page)
    #url = "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=2&filter_in_stock=1&filter_in_stock=1&page="+str(page)
    url = "https://www.dr.com.tr/"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi.decode('utf-8', 'ignore'),"html.parser")
    hrefs = soup.find_all("li",{"data-id":"yenicikan-click"})
    links = []
    for b in hrefs:
        links.append(b.find("a")["href"])
    return url+links[0]

#print(GetNewBookLinks())

def GetBookData():
    now = datetime.datetime.now()
    link,title,writer,translator,publisher,comment,language,isbn,version,hardcover,papertype,picture,category,pages,dimension="","","","","","","","","","","","","","",""
    #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows
    cursor = conn.cursor()
    book = GetNewBookLinks()
    try:
        response = requests.get(book)
        content = response.content
        soup = BeautifulSoup(content.decode('utf-8', 'ignore'),"html.parser")
    except:
        print("Connection problem")
    

    content = soup.find_all("div",{"class":"content"})
    for t in content:
        title = t.find("a")["title"]
        link = "https://www.dr.com.tr/" + t.find("a")["href"]
        writer = t.find_all("a",{"class":"who"})[0].text.strip()
        cursor.execute("SELECT distinct Id FROM WRITERS WHERE Name=?",(writer))
        writer = cursor.fetchone()
        if writer is None or len(writer) == 0:
                writer = t.find_all("a",{"class":"who"})[0].text.strip()
                cursor.execute("INSERT INTO WRITERS (Name, Update_Date) values (?,?)",(writer, now))
                cursor.commit()
                cursor.execute("SELECT distinct Id FROM WRITERS WHERE Name=?",(writer))
                writer = cursor.fetchone()


        
GetBookData()