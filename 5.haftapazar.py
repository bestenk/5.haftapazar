# __init__ constructor - yapıcı metot


class personel:
    isim    = ""
    soyisim = ""
    yas     = 0

    def __str__(self):
       return "{} {}".format(self.isim,self.soyisim)
    def __init__(self,firstname,lastname,age):
        self.isim = firstname
        self.soyisim = lastname
        self.yas = age


# __init__ metodunu kulladıdığımız için alttaki kodlra gerek yok
#personel = personel()
#personel.isim = "beste"
#personel.soyisim = "karademir"
#personel.yas = "20"

#print(personel)
#---------------------------------------------------

employee = personel("beste","karademir",20)
print(employee)

