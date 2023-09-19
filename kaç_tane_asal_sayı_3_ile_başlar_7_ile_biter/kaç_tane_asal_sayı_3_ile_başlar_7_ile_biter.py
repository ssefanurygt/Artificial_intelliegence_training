prime_list=list()
prime_list.append(2)
sayı=3
while True:
    prime=True
    for i in range(2,int(sayı**0.5)+1):
        if sayı%i==0:
            prime=False
            break
        
if prime==True:
    prime_list.append(sayı)
    if len(prime_list)==10000:
            sys.exit()
    sayı+=1
    print(prime_list)
    
    liste2=[]
for prime in prime_list:
    strprime= str(prime)
    if strsayı.startswith("3") and strsayı.endwith("7"):
        liste2.append(prime)
        print(liste2)
        print(len(liste2))
