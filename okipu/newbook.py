# - *- coding: utf- 8 - *-
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

def GetNewBookLinks(page):
    #url = "https://www.kitapyurdu.com/yeni-cikan-kitaplar/haftalik/2.html"
    url = "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=2&filter_in_stock=1&filter_in_stock=1&page="+str(page)
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi.decode('utf-8', 'ignore'),"html.parser")
    hrefs = soup.find_all("div",{"class":"cover"})
    links = []
    for b in hrefs:
        links.append(b.find("a")["href"])
    return links

def GetBookData():
    now = datetime.datetime.now()
    title,writer,translator,publisher,comment,language,isbn,version,hardcover,papertype,picture,category,pages,dimension="","","","","","","","","","","","","",""
    for x in range(1,26):    
        for book in GetNewBookLinks(x):
            response = requests.get(book)
            content = response.content
            soup = BeautifulSoup(content.decode('utf-8', 'ignore'),"html.parser")
            title = soup.find_all("h1",{"class":"product-heading"})[0].text.strip()
            writer = soup.find_all("span",{"itemprop":'name'})[0].text.strip()
            comment = soup.find_all("span",{"itemprop":"description"})[0].text

            if soup.find_all("span",{"itemprop":"name"}) is not None and len(soup.find_all("span",{"itemprop":"name"})) > 0:
                publisher = soup.find_all("span",{"itemprop":"name"})[0].text.strip()
            else:
                publisher = ""

            #category = soup.find_all("div",{"class":"grid_6 omega alpha section"})[0].text.lstrip("İlgili Kategoriler:\nKitap »").split()[0]
            if soup.find_all("div",{"class":"grid_6 omega alpha section"}) is not None and len(soup.find_all("div",{"class":"grid_6 omega alpha section"})) > 0:
                category = soup.find_all("div",{"class":"grid_6 omega alpha section"})[0].text.lstrip("İlgili Kategoriler:\nKitap »").split()[0]
            else:
                category = ""
            
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
                    dimension = say[16].text.replace("\n","").strip()
                elif len(say) == 16:
                    isbn = say[3].text.replace("\n","").strip()
                    version = say[5].text.replace("\n","").strip()
                    language = say[7].text.replace("\n","").strip()
                    pages = say[9].text.replace("\n","").strip()
                    hardcover = say[11].text.replace("\n","").strip()
                    papertype = say[14].text.replace("\n","").strip()
                    dimension = say[15].text.replace("\n","").strip()
                elif len(say) == 20:
                    translator = say[1].text.replace("\n","").strip()
                    isbn = say[7].text.replace("\n","").strip()
                    version = say[9].text.replace("\n","").strip()
                    language = say[11].text.replace("\n","").strip()
                    pages = say[13].text.replace("\n","").strip()
                    hardcover = say[15].text.replace("\n","").strip()
                    papertype = say[18].text.replace("\n","").strip()

            picture = isbn+".jpg"
            dir_path = os.path.dirname(os.path.realpath(__file__))
            piclink = soup.find_all("div",{"class":"image"})
            for plink in piclink:
                piclink = plink.find("a")["href"]

        
            filename = dir_path+"\\"+ picture
            urllib.request.urlretrieve(piclink, filename)
            
            
            session = ftplib.FTP("37.230.108.55","okipunet","zP1*S6po")
            session.cwd("/httpdocs/cache/")
            file = open(filename,"rb")
            session.storbinary("STOR " + picture, file)
            file.close()
            session.quit()
            try:
                conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows
                #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
                cursor = conn.cursor()
                cursor.execute("select Id, Title, Writer, Translator, Isbn, Comment from BOOKS where Title=? or Isbn=?", (title, isbn))
                repeated = cursor.fetchall()
            
        
                if len(repeated) == 0:
                    cursor.execute("SELECT Id FROM BOOK_CATEGORIES WHERE CategoryName=?",(category))
                    category = cursor.fetchone()
                    if category is None:
                        category = 25
                    else:
                        category = category.Id

                    version = re.findall("[0-9]", version)

                    cursor.execute("INSERT INTO BOOKS (Title,Writer,Translator,Publisher,Comment,Language,Isbn,BookEdition,NumberofPages,HardcoverType,PaperType,\
                    ProductDimensions,BookCategory,KucukResimYol,BuyukResimYol,IsActive,Update_Date,Company) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (title,writer,translator,publisher,comment,language,isbn,version[0],pages,hardcover,papertype,dimension,category,picture,picture,True,now,"KITAPYURDU"))
                    conn.commit()
                    conn.close()
                    print(str(isbn) + " Aktarıldı...")
            except:
               print("dbde hata olştu")

            for f in glob.glob(dir_path+"\\*.jpg"):
                os.remove(f)
    print("Receive complated. waiting 3 hours...")
    sleep(3600 * 3) # 3 saatte bir

while True:
    GetBookData()
    
    