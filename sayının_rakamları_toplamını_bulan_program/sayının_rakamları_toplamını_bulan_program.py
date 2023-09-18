sayı=int(input("sayı giriniz :"))
toplam=0
geçici_sayı=sayı
str_sayı=str(sayı)
for rakam in str_sayı:   #stringe çevirerek yapma
    toplam+=int(rakam)
    print(toplam)
    


while geçici_sayı !=0:
    basamak=geçici_sayı%10  #alternatif çözüm
    toplam+=basamak
    geçici_sayı //=10 #tam sayı bölmesi
    print(toplam)
    
