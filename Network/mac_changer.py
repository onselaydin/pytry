# ifconfig eth0 down
# ifconfig eth0 hw ether 00:11:22:33:44:55
# ifconfig eth0 up
# ifconfig de mac değişimi görülüyor.
#https://docs.python.org/2/library/subprocess.html
#https://regex101.com/


#işletim sistemi komutlarını kullabiliriz.
import subprocess
#kendi seçeneklerimizi ekleyebiliriz. Kullanıcıdan veri alabiliriz.
#python mac_changer.py -i eth0
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest = "interface",help="interface değiştirici")
parse_object.add_option("-m","--mac",dest="mac_address",help="yeni mac adres")
(user_inputs,arguments) = parse_object.parse_args()
user_interface = user_inputs.interface
user_mac = user_inputs.mac_address

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
subprocess.call(["ifconfig",user_interface,"up"])

"""
subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])
"""