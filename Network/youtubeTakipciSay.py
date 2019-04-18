import urllib.request
import json

#CREATED BY: "Mustafa AlRubiy"
#MAY 4, 2018

name=input("Enter username:  ")
key = "YOUR KEY GOES HERE"

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉")