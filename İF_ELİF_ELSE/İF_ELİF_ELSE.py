if True:
    print("koşul doğru")
    print("hala if bloğunun içindeyiz")
    
a=5
b=5
if a==b:
    print("a=b")
   
    
renk= "pembe"
if renk=="mavi":
    print("renk doğru")
else:
    print("renk yanlış")

a=8
b=4
c=10
if a<b or c>a or b>a:
    print("koşul doğru")
else:
    print("koşul yanlış")
    
liste=[1,2,3,4,5,6,7,8]
k=5
l=12
if k in liste:    #in anahtarı içinde mi değil mi ona bakar.
    print("listede")
else:
    print("listede değil")
    
m="python"
x="pyto"
x+="n"
print(m) #ikisi de python yazdırır ama hafızadaki boyutları farklıdır.
print(x)
if a is x:   #is anahtar kelimesinin doğru olması için kıyaslanan 
    print("a=b") #iki değişkenin hafızada aynı yeri tutması gerekiyor.
else:
    print("a!=b")

  

    