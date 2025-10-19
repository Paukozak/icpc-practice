import math

N=int(input())
W, L, Tx, Ty = map(int, input().split())

A=[]
R=[]
Tejin=[]
Tejin.append(Tx)
Tejin.append(Ty)
distA=[]
distR=[]

for i in range(N):
    l = list(map(int, input().split()))
    A.append(l)

for j in range(N):
    l = list(map(int, input().split()))
    R.append(l)
menorA=-1
menorR=-1
temp=0
for k in range(N):
    
    dA=math.dist(A[k],Tejin)
    dR=math.dist(R[k],Tejin)
    #print(dA)
    #print(dR)
<<<<<<< HEAD
    
    distA.append(dA)
    distR.append(dR)
    
minA=min(distA)
minR=min(distR)

puntos=0
if minA<minR:
    winner="A"
    puntos+=1
    distA.remove(minA)
    if len(distA!=0):
        minA=min(distA)
    
    while len(distA)!=0 and minA<minR:
        puntos+=1
        distA.remove(minA)
        if len(distA)>0:
            minA=min(distA)
    
else:
    winner="R"
    puntos+=1
    distR.remove(minR)
    if len(distR!=0):
        minR=min(distR)
    
    while len(distR)!=0 and minR<minA:
        puntos+=1
        distR.remove(minR)
        if len(distR)>0:
            minR=min(distR)


=======
    if k==0:
        menorA=dA 
        menorR=dR
        if dA<dR:
            menor=dA
            #print(menor)
        else:
            menor=dR
            #print(menor)
    if k!=0 and dA<menorA:
        menorA=dA
        #print("a mas chico")
        if menorA<menor:
            menor=menorA
            #print("cambio")
    if k!=0 and dR<menorR:
        menorR=dR    
        #print("R mas chico")        
        if menorR<menor:
            menor=menorR
            #print("cambio")

puntosA=0
puntosR=0
#print(menorA)
#print (menorR)
#print (menor)
for i in range (N):
    if menorA<menorR:
        if math.dist(A[i],Tejin)<menorR:
            puntosA+=1
    else:
        if math.dist(R[i],Tejin)<menorA:
            puntosR+=1
>>>>>>> f5fd42aab666759ff89f86324f651fed88d2099c

#print(pA)
#print(pR)
<<<<<<< HEAD
result.append(winner)
result.append(puntos)
=======
if menorA<menorR:
    ganador="A"
    puntos=puntosA
else:
    
    ganador="R"
    puntos=puntosR
>>>>>>> f5fd42aab666759ff89f86324f651fed88d2099c

print(ganador, puntos)

       
            
    
        
        
    
    
    