class Worker():
    def __init__(self, isim,maas,departman):
        print("çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("çalışan sınıfının bilgileri")
        print("isim : {}\nMaaş : {}\nDepartman: {}\n ".format(self.isim, self.maas, self.departman))
    
    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman