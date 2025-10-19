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

for k in range(N):
    
    dA=math.dist(A[k],Tejin)
    dR=math.dist(R[k],Tejin)
    #print(dA)
    #print(dR)
    
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



result=[]
#print(pA)
#print(pR)
result.append(winner)
result.append(puntos)

print(" ".join(map(str, result)))

       
            
    
        
        
    
    
    