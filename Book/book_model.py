class Book():
        def __init__(self,isim,yazar,sayfa_sayisi,tur):
                print("init fonksiyonu")
                self.isim = isim
                self.yazar = yazar
                self.sayfa_sayisi = sayfa_sayisi
                self.tur = tur
        def __str__(self):
                return "isim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)
        def __len__(self):
                return self.sayfa_sayisi
        def __del__(self):
                print("Kitap siliniyor")