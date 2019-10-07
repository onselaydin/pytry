# netdiscover -- linux ağ tarayıcı komutu.
# pip install scapy yada pip3 install scapy
# https://scapy.readthedocs.io/en/latest/
import scapy.all as scapy
#scapy.ls(scapy.ARP()) bilgi almak istediğimiz metodu ls içine yazıyoruz.
arp_request_package = scapy.ARP(pdst="10.17.10.0/24") # arp paketi oluşturuyoruz.

broadcast_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") ## ff broadcast yap.

combined_package =  broadcast_package/arp_request_package # birleştirdir

(answered_list, unanswered_list) = scapy.srp(combined_package,timeout=1) # cevap vermeyenleride göster.

#print(list(answered_list))

answered_list.summary()
#unanswered_list.summary()