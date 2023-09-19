metin=input("metni giriniz :")

sözlük=dict()

for harf in metin:
    if harf in sözlük:
        sözlük[harf] += 1
    else:
        sözlük[harf]=1
        for harf,adet in sözlük.items():
               print(harf,adet)
            
        
#ekrandan okunan bir metinde a harflerini büyük yapan bir program yazınız.

metin=input("bir metin giriniz :")
metin2=""
for harf in metin:
    if harf=="a":
        metin2+= "A"  #stringlerdeki toplama işlemi yanına yazmak demek.
    else:
        metin2+= harf
    print(metin2)
         

        
