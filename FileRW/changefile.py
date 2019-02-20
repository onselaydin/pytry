#with open("test.txt","r+",encoding="utf-8") as file: # r+ oku yaz. bu örnekte imlecin konumlandığı yerden itibaren ekleme yapıyor.
#    file.seek(5)
#    file.write("Ayşe")
#print(file.read)

with open("test.txt","a",encoding="utf-8") as file: #append
    file.write("polat aydın\n")
with open("test.txt","r",encoding="utf-8") as file:
    print(file.read())