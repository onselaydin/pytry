def ekstra(fonk):

    def wrapper(sayılar):
        çift_toplamı = 0
        çift_sayılar = 0
        tek_toplamı = 0
        tek_sayılar = 0
        for sayı in sayılar:
            if (sayı % 2 == 0 ):
                çift_sayılar +=1
                çift_toplamı += sayı
            else:
                tek_sayılar += 1
                tek_toplamı += sayı
        print("Çift Sayıların Ortalaması:", çift_toplamı/çift_sayılar)
        fonk(sayılar)
        print("Tek Sayıların Ortalaması:", tek_toplamı / tek_sayılar)
    return wrapper

@ekstra
def ortalama(sayılar):
    toplam = 0

    for i in sayılar:

        toplam += i

    print("Genel Ortalama:",toplam/len(sayılar))

ortalama([1,2,3,4,5,6,7,8,9,10])
