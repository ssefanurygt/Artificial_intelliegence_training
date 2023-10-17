from re import T
import time


zaman=time.time()
print(zaman) #epoch :programlama dillerinin zamanın başlangıcı kabul ettikleri (01.01.1970) tarihinden itibaren geçen zamanı saniye olarak yazdırır.


başlangıç=time.time()
liste=[]
for i in range(1000000):
    liste.append(i)
bitiş=time.time()
print(bitiş-başlangıç)  #program çalışırken aradan geçen zamanı gösterir.
  

zamann=time.ctime() #içi boş olursa şuan içinde bulunduğumuz zamanı verir.içine değer yazarsak şuanki zamana o değer kadar saniye ekler.
print(zamann)


zamannn=time.localtime() #zamanı time tuple olarak yani zamanı değişik formatta tüm bileşenleriyle(ay,yıl,saat...) olarak verir
print(zamannn)


zzaman=time.asctime()#localtime'ı kullanışlı hale getirir.
print(zzaman)


zamaan=time.strftime("%y:%m:%d") #içine girilen parametrenin o anki değerini döndürür.(yıl,ay,gün)
print(zamaan)


print("program başlatıldı")
time.sleep(3) #çalıştırılan programın belirtilen değer kadar durmasını sağlar.
print("program sonlandı")


