sayı=int(input("sayı giriniz"))
prime=True #girilen sayıyı en başta asal kabul ettik sonra sayıdan küçük sayılara bölünürlüğünü kontrol ettik
for i in range(2,sayı):
    if sayı%i == 0:
        prime=False
        break
if prime==True:
    print(f"{sayı} sayısı asaldır")
else:
    print(f"{sayı} sayısı asal değildir")
