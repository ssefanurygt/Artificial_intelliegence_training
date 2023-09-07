renkler,= ["mavi","yesil","sari","siyah"]
print(type(renkler))
print(len (renkler))
print(renkler[2])

renkler.append("gri")
print(renkler)

renkler.insert(1,"kirmizi")
print(renkler)

renkler.remove("sari")
print(renkler)

renkler2= ["mor","truncu"]
renkler.extend(renkler2) #renkleer2'nin elemanlarını renklere ekleer
print(renkler)

silinen= renkler.pop() #sondaki elemanı siler
print(silinen)

renkler.reverse()
renkler.sort() #listeyi alfabetik sıralar
renkler.sort(reverse= True)
print(renkler)

liste2=sorted(renkler)
print(liste2)
print(renkler)
   

renkler= ["mavi", "yesil", "sari", "siyah"]
sayi=[2,9,7,4,3,65]

print(min(renkler))
print(max(sayi))

print(list(enumerate(renkler)))
print("gri" in renkler)

stringrenkler= " - ".join(renkler)
print(stringrenkler)

renkler2= stringrenkler.split(" - ")
print(renkler2)