import random 
secenek={"tas,kagit,makas"}
tas=secenek[0]
kagit= secenek[1]
makas=secenek[2]
print("tas,kagit,makas oyununa ho�geldiniz /n oyunu bitirmek i�in e tusuna basiniz ")


while(True):
    secim=input("seciminizi yapiniz: ")
    bil_secim=random.choice(secenek)
    if secim==tas:
            if bil_secim==tas:
                print("bilgisayar�n se�imi tas, oyun berabere")
            elif bil_secim==kagit:
                print("bilgisayar�n se�imi ka��t, bilgisayar kazand�")
            else:
                print("bilgisayar�n se�imi makas, bilgisayar kazand�")
    if secim==kagit:
            if bil_secim==tas:
                print("bilgisayar�n se�imi tas, kazand�n")
            elif bil_secim==kagit:
                print("bilgisayar�n se�imi ka��t, berabere")
            else:
                print("bilgisayar�n se�imi makas, bilgisayar kazand�")
    if secim==makas:
            if bil_secim==tas:
                print("bilgisayar�n se�imi tas, kazand�n")
            elif bil_secim==kagit:
                print("bilgisayar�n se�imi ka��t, kazand�n")
            else:
                print("bilgisayar�n se�imi makas, berabere")