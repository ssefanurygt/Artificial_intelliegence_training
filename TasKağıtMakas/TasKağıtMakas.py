import random 
secenek={"tas,kagit,makas"}
tas=secenek[0]
kagit= secenek[1]
makas=secenek[2]
print("tas,kagit,makas oyununa hoşgeldiniz /n oyunu bitirmek için e tusuna basiniz ")


while(True):
    secim=input("seciminizi yapiniz: ")
    bil_secim=random.choice(secenek)
    if secim==tas:
            if bil_secim==tas:
                print("bilgisayarın seçimi tas, oyun berabere")
            elif bil_secim==kagit:
                print("bilgisayarın seçimi kağıt, bilgisayar kazandı")
            else:
                print("bilgisayarın seçimi makas, bilgisayar kazandı")
    if secim==kagit:
            if bil_secim==tas:
                print("bilgisayarın seçimi tas, kazandın")
            elif bil_secim==kagit:
                print("bilgisayarın seçimi kağıt, berabere")
            else:
                print("bilgisayarın seçimi makas, bilgisayar kazandı")
    if secim==makas:
            if bil_secim==tas:
                print("bilgisayarın seçimi tas, kazandın")
            elif bil_secim==kagit:
                print("bilgisayarın seçimi kağıt, kazandın")
            else:
                print("bilgisayarın seçimi makas, berabere")