#fonksyonlar tekrar tekrar yapacağımız işlemler için kullanacağımız kodu fonksyon Olarak tanımlayıp gereken durumda hazır olarak kullanmamızı sağlar. 
def selamla(isim):
    print("merhaba"+  isim)
    
selamla("ali")  #fonksyonu çağırırken fonksyon parametresine değer atanır.


def topla(x,y):
    print(f"x+y={x+y}")
topla(6,8)


def ort_hesapla(liste):
    toplam=sum(liste)
    adet=len(liste)
    ortalama=toplam/adet
    print(f"girilen sayıların ortalaması: {ortalama}")
ort_hesapla([5,9,7,32,45,70])
    
    
def büyük_harfe_çevir():
    metin= metin.upper()
    print(metin)
    
büyük_harfe_çevir("kahraman")


    
def selamlaa(mesaj,isim="anonim"):
    print(f"{mesaj} {isim}")
    
selamlaa("merhaba","elif") 