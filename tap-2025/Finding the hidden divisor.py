import math

N=int(input())
X=list(map(int, input().split()))
lista=set(X)
X.sort()

bandera=True
if N==1:
    if X[0]==1: #cuando viene un 1 solo y no se cual es
        print ('*')
    else:
        print (X[0], '1') #cuando viene un primo solo se que es el uno
elif (N==2) and (((math.sqrt(X[1]))%1)==0) and ((math.isqrt(X[1])) not in lista):
    print (X[1], int(math.sqrt(X[1])))
else:
    X.sort(reverse=True)
    mayor=X[0]
    for i in range (N):
        if ((mayor//X[i]) not in lista) and ((mayor%X[i])==0):   #cuando el mayor esta (verificamos diviendolo por el resto de numeros asegurandonos que sean divisones enteras)
            print (mayor, (mayor//X[i]))
            bandera=False
            break
    if bandera:
        div=mayor*X[(N-2)] #cuando el mayor no esta   
        print(div, div)


    
