
class ornek_sinif():
    a="degismez veri"
    def __init_(self) : #sinifi en basta baslatirken belirli ozelliklerde olmasini istiyorsam init'in icine yazarım. Constructor yani. Self parametresi ise sinifin her ozelligini diger bir sinifta kullanmak istersem yazarim.
        print("sınıf oluşturuldu")
        self.veri_1= "ornek sinif veri 1"  

    def veriyi_degistir(self):
        self.a="degisti"

sinifimiz= ornek_sinif()
print(sinifimiz.veri_1)

sinifimiz.veriyi_degistir()
print(sinifimiz.a)



class kus():
    def __init_(self):
        print(" kus sinifi olusturuldu")
        
    def senkimsin(self):
        print("sen kimsin")
        
    def yüzermisin(self):
        print("hayir")
        
    def renginne(self):
        print("sari")
        
class Karga(kus):
    def __init_(self):
        super().__init_()
        print("karga olsturuldu")
                              # override ettik.Üst sinif ozelliklerini kalitim alan alt sinifta degistirdik
    def yüzermisin(self):
        print("evet")
       
    def senkimsin(self):
        print("karga")
        
    def sesimkötümü(self):
        print("evet")
        
karga=Karga()
karga.yüzermisin()
karga.renginne()   #renginne fonksyonu override edilmedigi icin üst siniftaki oldugu gibi gecti.



















        
        

 