#http://www.timas.com.tr/kategori/yeni-cikan-kitaplar/
import requests
from bs4 import  BeautifulSoup
import datetime
from time import sleep
import pyodbc
import urllib.request
import os
import ftplib
import pyodbc

def GetNewBookLinks():
    url = "https://www.kitapyurdu.com/yeni-cikan-kitaplar/haftalik/2.html"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    hrefs = soup.find_all("div",{"class":"cover"})
    links = []
    for b in hrefs:
        links.append(b.find("a")["href"])
    return links

def GetBookData():
    title,writer,translator,publisher,comment,language,isbn,version,hardcover,papertype,picture,category,pages="","","","","","","","","","","","",""
    for book in GetNewBookLinks():
        response = requests.get(book)
        content = response.content
        soup = BeautifulSoup(content,"html.parser")
        title = soup.find_all("h1",{"class":"product-heading"})[0].text.strip()
        writer = soup.find_all("span",{"itemprop":'name'})[0].text.strip()
        comment = soup.find_all("span",{"itemprop":"description"})[0].text
        publisher = soup.find_all("span",{"itemprop":"name"})[1].text.strip()
        category = soup.find_all("div",{"class":"grid_6 omega alpha section"})[1].text.lstrip("İlgili Kategoriler:\nKitap »").split()[0] #Buradan devam et.....»
        details = soup.find_all("table",{"class":"attribute"})
        for td in details:
            say = td.find_all("td")
            if len(say) == 18:
                translator = say[1].text.replace("\n","").strip()
                isbn = say[5].text.replace("\n","").strip()
                version = say[7].text.replace("\n","").strip()
                language = say[9].text.replace("\n","").strip()
                pages = say[11].text.replace("\n","").strip()
                hardcover = say[13].text.replace("\n","").strip()
                papertype = say[15].text.replace("\n","").strip()
            elif len(say) == 16:
                isbn = say[3].text.replace("\n","").strip()
                version = say[5].text.replace("\n","").strip()
                language = say[7].text.replace("\n","").strip()
                pages = say[9].text.replace("\n","").strip()
                hardcover = say[11].text.replace("\n","").strip()
                papertype = say[14].text.replace("\n","").strip()
            if len(say) == 20:
                translator = say[1].text.replace("\n","").strip()
                isbn = say[7].text.replace("\n","").strip()
                version = say[9].text.replace("\n","").strip()
                language = say[11].text.replace("\n","").strip()
                pages = say[13].text.replace("\n","").strip()
                hardcover = say[15].text.replace("\n","").strip()
                papertype = say[17].text.replace("\n","").strip()

        picture = isbn+".jpg"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        piclink = soup.find_all("div",{"class":"image"})
        for plink in piclink:
            piclink = plink.find("a")["href"]

        """
        filename = dir_path+"\\"+ picture
        urllib.request.urlretrieve(piclink, filename)
        
        
        session = ftplib.FTP('ftp://37.230.108.55/httpdocs/cache/','okipunet','zP1*S6po')
        file = open(filename,'rb')
        session.storbinary('STOR '+filename, file)
        file.close()
        session.quit()
        """
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows
        #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
        cursor = conn.cursor()
        cursor.execute("select Id, Title, Writer, Translator, Isbn, Comment from BOOKS where Title=? or Isbn=?", (title, isbn))
        repeated = cursor.fetchall()
        
        if len(repeated) == 0:

            cursor.execute("SELECT * FROM BOOK_CATEGORIES WHERE CategoryName=?",(category))
            category = cursor.fetchone()
            if category[0] == None:
                category = 25



            #cursor.execute("INSERT INTO BOOKS (Title,Writer,Translator,Publisher,Comment,Language,Isbn,BookEdition,NumberofPages,HardcoverType,PaperType,\
            #ProductDimensions)")

GetBookData()