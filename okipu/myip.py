from pymongo import MongoClient
import requests
from bs4 import  BeautifulSoup

url = "https://ping.eu"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
td = soup.find_all("td",{"class":"txt14"})
for b in td:
    print(b.find("b").text)
