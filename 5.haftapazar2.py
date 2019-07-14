# Inheritance

class calisan():
    def __init__(self, isim, soyisim, maas, depatman, yas = 20):
        print("çalışan sınıfın yapıcı metodu çalıştı!")
        self.isim      = isim
        self.soyisim   = soyisim
        self.yas       = yas
        self.maas      = maas
        self.departman = depatman
    def __str__(self):
        return "{} {} {}".format(self.isim,self.soyisim,self.yas)

    def bilgigoster(self):
        print("calısan sınıfına ait bilgiler gösterilmektedir")
        print("- isim       : {}\n- soyisim    : {}\n- departman  : {}\n- maaş       : {}".format(
            self.isim,
            self.soyisim,
            self.departman,
            self.maas))
        print("-"*30)
    def zamyap(self,zam_oranı):
        print("çalışanın maaşına zam yapılmıştır ")
        maas = self.maas
        self.maas += zam_oranı
        print("{} personelin maası : {} tl den {} ye yükseldi.".format(self.isim + " "+self.soyisim,maas,self.maas))

    def departmanıdeğiştirildi(self,departman):
        print("çalışanın departmanı değiştirildi")
        departman = self.departman
        self.departman = departman
        print("{} personelin departmanı : {} departmanından {} departmanına geçiş yaptı.".format(self.isim +" "+self.soyisim,departman,self.departman))

#personelin maaşına zam yapıldığında veya departmanı değiştirildiğinde kullanıcıya eski ve yeni değerleri gösteriniz.
# x personeli > x departmanından y departmanına geçiş sağlandı
# çalışanın eski maaşı > çalışanın yeni maaşı




#yas parametresi olarak göndermezsek içerde tanımlı default değer geçerli olacaktır.
#personel = calisan("beste","karademir",777777,"öğrenci",20)

#personel = calisan("beste","karademir",777777,"öğrenci",20)

#print(personel)
#personel.zamyap(1000)
#personel.departmanıdeğiştirildi("mühendis")
#personel.bilgigoster()


class Yonetici(calisan):
    def __init__(self,isim, soyisim, maas, departman, yas, kisi_sayisi):
        print("yönetici sınıfı, yapıcı metodu çalıştı")
        self.isim        = isim
        self.soyisim     = soyisim
        self.departman   = departman
        self.maas        = maas
        self.kisi_sayisi = int(kisi_sayisi)
        self.yas         = yas


    def prin_base(self):
        for base in self.__class__.__bases__:
            print("miras alınan sınıf :", base.__name__)
    def __str__(self):
        return "{} {} {}".format(self.isim, self.soyisim, self.departman)

yonetici = Yonetici("ahmet","mehmet",9000,"sistem",35,20)
print(yonetici)
yonetici.prin_base()
yonetici.bilgigoster()
yonetici.zamyap(5000)
yonetici.departmanıdeğiştirildi("yazılım")
















