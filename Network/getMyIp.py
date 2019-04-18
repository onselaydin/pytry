from urllib import request

b = request.urlopen("https://api.ipify.org").read().decode('utf-8')

import platform
import socket

pc_details = platform.uname()
iploc = socket.gethostbyname(socket.gethostname())
name = socket.gethostbyaddr(iploc)[0]
print("Local ip: ", iploc)
print("Name: ", name)
print("")
print("$____________________________$")
print("External ip: ", b)
for n in pc_details:
    print("OS: ", pc_details[0])
    print("Release: ", pc_details[2])
    print("Name: ", pc_details[1])
    print("Version: ", pc_details[3])
    print("Machine: ", pc_details[4])
    print("Processor: ", pc_details[5])
    break
import json

url = "https://extreme-ip-lookup.com/json/"
ip_info = json.load(request.urlopen(url))
print("IP Geolocation Info =>\n")
for param, val in ip_info.items():
    print(f"{param.upper()}{' ' * (15 - len(param))}: {val if len(val) != 0 else 'NA'}")
print("$____________________________$")

import os
print(os.listdir("C:\\CompilerBIN\\"))