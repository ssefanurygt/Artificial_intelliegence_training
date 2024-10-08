import random 
liste= []
print("cekilisi baslatmak icin 'baslat', \n iptal etmek icin 'iptal' yaz")

while(True):
    try:
        giris=input("cekilise katiacak kisiler: ")
        if giris=="iptal":
            sor=input("kisiyi mi (kisi) cekilisi mi (cekilis) iptal etmek istiyorsunuz? ")
            if sor=="kisi":
                sor1=input("iptal edilmesini istediginiz kisiyi yaziniz: ")
                if sor1 in liste:
                   yer=liste.index(sor1)
                   liste.pop(yer)
                   print("kisi iptal edildi")


            elif sor=="cekilis":
                try:
                    while (True):
                        liste.pop()
                except:
                    print("cekilis iptal edildi")
        elif giris=="baslat":
               sor2=int(input("kac kisi kazanacak \n"))
               if len(liste)<sor2:
                print("kazanacak kisiler girilen kisi sayýsýndan fazla olamaz ")
                print("lütfen tekrar deneyin")
        else:
            liste.append(giris)
    except:
        print("hatali giris yaptiniz tekrar deneyiniz")
        
