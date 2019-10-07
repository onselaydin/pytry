#men in the middle yaptıktan sonra http trafiğini izlemek için
#pip install scapy_http  yüklemek lazım
#pip3 install scapy_http
#http://www.gokhanyuceler.com/python-dns-spoofing/


import scapy.all as scapy
from scapy_http import http

def listen_packets(interface):
    #scapy.sniff(iface="eth0") #eth0,wlan0 linux içindir
    #
    scapy.sniff(iface=interface,store=False,prn=analyz_packets)
    #prn = callback function

def analyz_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

listen_packets("eth0") # wlan0, eth0 ve any bazı örnekler
