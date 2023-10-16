#random modülü rastgele sayılar veya değerler üreten fonksyonları barındırır.
import random
for i in range(10):
    print(random.random) #random fonk.0-1 aralığında değer üretir

    print(random.uniform(10,30)) #uniform fonksyonu istenilen aralıkta değer üretir.
    print(random.randint(1,5)) #sadece randint fonksyonunda her iki sınır da dahil
  
print(random.randrange(1,10,2)) #1 ile başla 10a kadar ikişer ikişer git
    
liste =["sarı","beyaz","mavi","gri"]
print(random.choice(liste)) #verilen listeden rastgele eleman seçer.

random.shuffle(liste)#elemanların yerini değiştirir.
print(liste)

print(random.sample(liste,2)) #listeden iki elemanı örnekler





