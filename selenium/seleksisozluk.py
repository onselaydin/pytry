from selenium import webdriver
import time
import random
browser = webdriver.Chrome()
url = "https://eksisozluk.com/recep-tayyip-erdogan--95281?p="

pageCount = 1
entries = []
entryCount = 1
while pageCount <= 10:
    randomPage = random.randint(1,4423)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

for ent in entries:
    print(str(entryCount) + "*************************************")
    print(ent)
    entryCount += 1

browser.close()
