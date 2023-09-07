kume= {'mavi','sari','yesil','mor'}
print(kume)

#for renk in kume:
 #print(kume)    

kume.add("turuncu")
kume.remove("sari")  #remove metodu eleman kumede yoksa  hata verir yazdırmaz.
print(kume)

kume.discard("siyah")  #discart kumede olmayan elemanı kaldırmak istediğimizde hata vermeden listeyi aynen yazdıran metottur.
print(kume)


kume1= {'mavi','sari','yesil','mor'}

kume2= {'mor','turuncu','pembe','siyah','sari'}
print(kume1.intersection(kume2))   #iki kumenin kesişimi
print(kume1.union(kume2))  #iki kumenin birlesimini verir.
print(kume1.difference(kume2))

print( 'mavi' in kume1) #mavi kume1 de var mı (cevap true yada false) 


bosliste=[]  #boş liste oluşturur.
bosliste2= list() #boş liste oluşturur.

bosdemet1= ()  #ikisi de boş tuple açar
bosdemet2= tuple()

boskume= set()  #boş küme açar






