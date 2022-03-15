from random import choice
class mp3Calar():
    def __init__(self,sarkiListesi = []):
        self.suancalansarki = ""
        self.ses = 100
        self.sarkiListesi = sarkiListesi
        self.durum = True

    def sarkiSec(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{} {}".format(sayac, sarki))
            sayac += 1
        seciliceksarki = int(input("Seçmek İstediğiniz Şarkı Numarasını giriniz"))
        while seciliceksarki < 1 or seciliceksarki > len(self.sarkiListesi):
            seciliceksarki= int(input("Lütfen belirtilen aralıklarda bir numara giriniz ( 1 - {})".format(len(self.sarkiListesi))))

        self.suancalansarki = self.sarkiListesi[seciliceksarki-1]

    def sesArttir(self):
        if self.ses == 100:
            pass
        else:
            self.ses+= 10

    def sesAzalt(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10

    def rastgeleSarkiSec(self):
        rastgele_sarki = choice(self.sarkiListesi)
        self.suancalansarki = rastgele_sarki

    def sarkiEkle(self):
        sanatci = input("Sanatçıyı/Grubu Giriniz")
        sarki = input("Şarkıyı giriniz")
        self.sarkiListesi.append(sanatci + " - " + sarki)

    def sarkiSil(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{} {}".format(sayac, sarki))
            sayac += 1
        siliceksarki = int(input("Silmek İstediğiniz Şarkı Numarasını giriniz"))
        while siliceksarki < 1 or siliceksarki > len(self.sarkiListesi):
             siliceksarki = int(input("Hatalı seçim yaptınız.Belirtilen aralıklarda seçin yapınız(1-{})".format(len(self.sarkiListesi))))
        self.sarkiListesi.pop(siliceksarki - 1)




    def menugoster(self):
        print("""
(-Mert Kağan Toy Mp3 Çalara Hoş Geldiniz-)
Şarkı Listesi = {}
Şuan Çalan Şarkı = {}
Ses Düzeyi {}

1)Şarkı Seç
2)Ses Arttır
3)Ses Azalt
4)Rastgele Şarkı Seç
5)Şarkı Ekle
6)Şarkı Sil
7)Kapa
""".format(self.sarkiListesi,self.suancalansarki,self.ses))


    def secim(self):
        sec = int(input("Seçiminizi Giriniz:"))

        while sec<1 or sec>7:
            sec = int(input("Hatalı secim yaptınız.Belirtilen aralıklarda bir değer giriniz(1-7)"))

        return sec

    def calistir(self):
        self.menugoster()
        sec = self.secim()
        if sec == 1:
            self.sarkiSec()
        if sec == 2:
            self.sesArttir()
        if sec == 3:
            self.sesAzalt()
        if sec == 4:
            self.rastgeleSarkiSec()
        if sec == 5:
            self.sarkiEkle()

        if sec == 6:
            self.sarkiSil()

        if sec == 7:
            print("Bizi Tercih Ettiğiniz İçin Teşşekkür Ederiz!!")
            self.kapa()


    def kapa(self):
        self.durum = False


mp3calar = mp3Calar()
while mp3calar.durum:
    mp3calar.calistir()

