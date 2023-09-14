sayı=int(input("sayı giriniz :"))
bölen_sayısı=0
 
for i in range(1,sayı+1):
    if sayı%i == 0:
        bölen_sayısı += 1

print(f"{sayı} sayısının {bölen_sayısı} kadar böleni vardır")




