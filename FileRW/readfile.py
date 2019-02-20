try:
    with open("test.txt","r",encoding="utf-8") as file:
        print(file.tell()) ## imleç nerede
        file.seek(20) # imleci 20. byte(karakter) götür.
        icerik = file.read(5) #imleç 20 den sonra 5 karakter al
        print(icerik)
        print(file.tell())

        #for i in file:
        #    print(i, end = "")
except:
    print("Hata var")