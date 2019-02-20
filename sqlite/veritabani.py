import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT, Yazar TEXT, Yayinevi TEXT, Sayfa INT)")
    con.commit()
#tablo_olustur()
def veri_ekle():
    cursor.execute("insert into kitaplik values('istanbul hatırası','Ahmet Ümit','Everest',565)")
    con.commit()
#veri_ekle()
def veri_ekle2(isim,yazar,Yayinevi,sayfa_sayisi):
   cursor.execute("insert into kitaplik values(?,?,?,?)",(isim,yazar,Yayinevi,sayfa_sayisi))
   con.commit()

isim = input("isim:")
yazar = input("Yazar:")
Yayinevi = input("Yayınevi:")
sayfa_sayisi = input("Sayfa Sayısı:")

veri_ekle2(isim,yazar,Yayinevi,sayfa_sayisi)

cursor.close()

