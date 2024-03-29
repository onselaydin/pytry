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
    #https://canyayinlari.com/kitaplar/?SayfaNo=1
    #url = "https://www.kitapyurdu.com/index.php?route=product/category&path=128_159&filter_in_stock=1&page="+str(page)
    #url = "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=2&filter_in_stock=1&filter_in_stock=1&page="+str(page)
    url = "https://www.kitapyurdu.com/yeni-cikan-kitaplar/haftalik/2.html"
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
    #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql11.turhost.com;PORT=1433;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #linux
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=mssql11.turhost.com;DATABASE=Okipu101_db;UID=okipusa;PWD=u5C/4Sc}') #windows
    cursor = conn.cursor()
    for x in range(1,25):   
        for book in GetNewBookLinks(x):
            sleep(5)
            try:
                response = requests.get(book)
                content = response.content
                soup = BeautifulSoup(content.decode('utf-8', 'ignore'),"html.parser")
            except:
                print("Connection problem")

            if soup.find_all("h1",{"class":"product-heading"}) is not None and len(soup.find_all("h1",{"class":"product-heading"}))>0:
                title = soup.find_all("h1",{"class":"product-heading"})[0].text.strip()
            else:
                title = "" 

            writer = soup.find_all("span",{"itemprop":'name'})[0].text.strip()

            cursor.execute("SELECT distinct Id FROM WRITERS WHERE Name=?",(writer))
            writer = cursor.fetchone()

            if writer is None or len(writer) == 0:
                writer = soup.find_all("span",{"itemprop":'name'})[0].text.strip()
                cursor.execute("INSERT INTO WRITERS (Name, Update_Date) values (?,?)",(writer, now))
                cursor.commit()
                cursor.execute("SELECT distinct Id FROM WRITERS WHERE Name=?",(writer))
                writer = cursor.fetchone()


            comment = soup.find_all("span",{"itemprop":"description"})[0].text

            if len(soup.find_all("span",{"itemprop":"name"})) >= 0:
                publisher ="Kollektif"
            elif soup.find_all("span",{"itemprop":"name"}) is not None and len(soup.find_all("span",{"itemprop":"name"})) > 0:
                publisher = soup.find_all("span",{"itemprop":"name"})[1].text.strip()
            else:
                publisher = "Kollektif"

            cursor.execute("SELECT distinct Id FROM PUBLISHERS WHERE Name=?",(publisher))
            publisher = cursor.fetchone()
            if publisher is None or len(publisher) == 0:
                if soup.find_all("span",{"itemprop":"name"}) is not None and len(soup.find_all("span",{"itemprop":"name"})) > 0:
                    publisher = soup.find_all("span",{"itemprop":"name"})[1].text.strip()
                else:
                    publisher = "Kollektif"
                cursor.execute("INSERT INTO PUBLISHERS (Name, Update_Date) values (?,?)",(publisher, now))
                cursor.commit()
                cursor.execute("SELECT distinct Id FROM PUBLISHERS WHERE Name=?",(publisher))
                publisher = cursor.fetchone()
     


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

            try:
                filename = dir_path+"\\"+ picture
                urllib.request.urlretrieve(piclink, filename)
            except:
                print("picture link not read...")
            
            try:
                session = ftplib.FTP("37.230.108.55","okipunet","zP1*S6po")
                session.cwd("/httpdocs/cache/")
                file = open(filename,"rb")
                session.storbinary("STOR " + picture, file)
                file.close()
                session.quit()
            except:
                print("ftp error...")
           
            try:
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
                    if len(re.findall("[0-9]",pages)) == 0:
                        pages = 0
                        
                    
                    cursor.execute("INSERT INTO BOOKS (Title,Writer,Translator,Publisher,Comment,Language,Isbn,BookEdition,NumberofPages,HardcoverType,PaperType,\
                    ProductDimensions,BookCategory,KucukResimYol,BuyukResimYol,IsActive,Update_Date,Company) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (title,writer[0],translator,publisher[0],comment,language,isbn,version[0],pages,hardcover,papertype,dimension,category,picture,picture,True,now,"KITAPYURDU"))
                    conn.commit()
                    
                    print(str(isbn) + " Imported...")
            except pyodbc.Error as err:
               print(err)

            for f in glob.glob(dir_path+"\\*.jpg"):
                os.remove(f)
    conn.close()
    print("Receive complated. waiting 3 hours...")
    sleep(3600 * 2) # 2 saatte bir

while True:
    GetBookData()
    
    