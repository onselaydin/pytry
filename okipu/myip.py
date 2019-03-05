from pymongo import MongoClient
import requests
from bs4 import  BeautifulSoup
import datetime
from time import sleep

def GetPostIp():
    url = "https://ping.eu"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    td = soup.find_all("td",{"class":"txt14"})
    ip = ""
    for b in td:
        ip = b.find("b").text
        print(b.find("b").text)

    client = MongoClient("mongodb://movie_user:abcd1234@ds213645.mlab.com:13645/movieapi")
    mydb = client['movieapi']
    mycol = mydb["homeip"]

    post = {"ip": ip, "date": datetime.datetime.utcnow()}
    x=mycol.insert_one(post)
    print("İşlem Tamam")
    sleep(1800)
while True:
    GetPostIp()