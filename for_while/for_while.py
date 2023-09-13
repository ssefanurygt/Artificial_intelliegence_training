#döngüler bir listedeki her elemana aynı işlemi yaptıran yapılardır.
liste=[1,2,3,4,5,6,10,12]
for i in liste:
    print(i)
                      #bir işlemi tekrar etmek istersek range fonksiyonunu kullanırız.
for rakam in range(0,10,2): #0'dan 0 dahil 10'a kadar olan ssyıları ikişer ikişer yazdırır.
    print(rakam)
    

sonuç=1
for i in range(0,10):
    sonuç*=2    
print(sonuç)


liste1=["a","b","c","d","e"]
liste2=[1,2,3]
for harf in liste1:
    for rakam in liste2:
        print(harf,rakam) 
    

listee=[1,2,3,4,5,6,7,8,9]
for i in listee:
    if i ==4:
     continue #döngünün bir sonraki elemena geçmesini sağlar.
    print(i)
    

for sayı in listee:
    if sayı==5:
       break
    print(sayı)
    

liste=range(100)
for i in liste:
    if i%3 != 0:
       continue
    if i==81:
       break
    print(i)
    

#while döngüsü belirli bir koşul sağlandığı sürece çalışan bir döngüdür.
x=2
y=3
while x*y< 100:
   print(x,y)
   x+=2
   y+=2
 
   
w=1
while True:
    print(w)
    w+=1
    if w==1000:
        break
        

while True:  #tek sayıları yazdırma.
    if w % 2 == 0:
        w+=1
        continue
    print(w) 
    w+=1
    if w==1000:
       break
