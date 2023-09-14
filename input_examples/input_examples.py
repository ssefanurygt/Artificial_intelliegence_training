sayı=input("bir sayı giriniz") 
print(sayı) #ekrandan alınan sayılar otomatik string algılanır,sayılarla işlem yapmak için int'e çevirmek gerekir.


sayı=int(sayı) #ya da int(input("sayı giriniz)) şeklinde çevrilir
print(type(sayı))

faktorıyel= 1

for i in range(1, sayı + 1):
    faktorıyel*=i
    print(faktorıyel)
    
i=2
while i<=sayı:
        faktorıyel*=i
        i+=1
        print(faktorıyel)