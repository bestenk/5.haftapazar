a = 40 # değeri 40 olan sayısal bir <class 'class'> tipinde bir değişken tanımladık

b = a   # b değişkeni tanımlayıp referansını a değişkeninden aldık.
c = [b] # c değişkeni tanımlayıp <class 'list'> b değerini refernas olarak verdik

print(type(a))
print(a)

del a     # a değişkeninin referansını sildik

b =100    # b değerin 100 değerini vererek üzerinde yer alan 40 değerini değiştirdik
print(type(c))
c[0] =-1  # c listesinin 0. elemanının değerini -1 olarak değiştirdik 40 değerini sildik ve a değişkenine ait hiç bir referans kalmamıştır
print(c[0])



class point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"heap üzerinden silindi")

pt1 = point()
pt2 = pt1
pt3 = pt1

print(id(pt1), id(pt2), id(pt3))  # nesnenin ram adresinin ekrana yazdırılması
# 22940912 => pt1
# 22940912 => pt2
# 22940912 => pt3

del pt1
del pt2
del pt3
print()

# id() nesnenin kimliğini döndürür nesne yaşam ömrü boyunca benzersiz ve sabit olacağı garantilenen (unig) bit tam sayıdır bitibrinden benzersiz iki nesne aynı değere sahip olabilrilerr