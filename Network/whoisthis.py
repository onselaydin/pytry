import whois
import sys
import time


whois_list = sys.argv[1]
site_list = []

with open(whois_list, 'r') as p:
    for line in p:
        site_list.append(line.rstrip('\n'))
        
for site in site_list:
    w = whois.whois(site)
    
    if w['org'] is not None:
        print("[+] site: " + str(site) + "\n[+] owner-name: "  + str(w['name']) + "\n[+] org: " + str(w['org']))
        print("--------------------------------------------------------------")
        
        time.sleep(3)