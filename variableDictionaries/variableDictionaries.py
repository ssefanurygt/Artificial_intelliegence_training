#birinci kelime anahtar eşleştirdiğimiz ise değer (key-value)

kişi= {"isim":"ali","yaş":"40","eğitim":"lise","cinsiyet":"erkek"} #key=isim value=ali  sözlüklerde key string veya int olmak zorunda value her şey olabilir.
print(kişi)
print(kişi["isim"]) #sözlüklerde index yok

kişi["isim"]="ahmet"
print(kişi["isim"])

kişi.update({"yaş":"42","eğitim":"üniversite"})#aynı anda iki key güncelleme
print(kişi)

kişi["ID"]=12345
print(kişi)


del kişi["cinsiyet"]
print(kişi)

for x in kişi: #key'leri yazdırdı
 print(x)
 print(kişi[x])#değerlerle birlikte yazdırdı.
  

 print(kişi.keys()) #sadece keyler
 print(kişi.values()) #sadece değerleri yazdı
print(kişi.items()) #keyleri valu ile eşleştirip yazdırdı.


for k,v in kişi.items():
    print(k,v)
    
print(kişi.get("cinsiyet")) #istediğimiz key yoksa hata döndürmemesi için get kullanılır.istenen key varsa değerini döndürür.
print(kişi.get("isim"))
  