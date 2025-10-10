import math

N=int(input())
W, L, Tx, Ty = map(int, input().split())

A=[]
R=[]
Tejin=[]
menor=-1
Tejin.append(Tx)
Tejin.append(Ty)
pA=0
pR=0

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

#print(pA)
#print(pR)
if menorA<menorR:
    ganador="A"
    puntos=puntosA
else:
    
    ganador="R"
    puntos=puntosR

print(ganador, puntos)

       
            
    
        
        
    
    
    