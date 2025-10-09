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

for k in range(N):
    
    dA=math.dist(A[k],Tejin)
    dR=math.dist(R[k],Tejin)
    #print(dA)
    #print(dR)
    if menor==-1:
        if dA<dR:
            pA+=1
            menor=dA
        else:
            #print("sume1")
            pR+=1
            menor=dR
    else:
        if dA<menor:
            if dA<dR:
                pA+=1
                menor=dA
            else:
                #print("sume 1")
                pR+=1
                menor=dR
        else:
            if dR<menor:
                #print("sume1")
                pR+=1
                menor=dR
                

result=[]
#print(pA)
#print(pR)
if pA>pR:
    result.append("A")
    result.append(pA)
else:
    result.append("R")
    result.append(pR)

print(" ".join(map(str, result)))

       
            
    
        
        
    
    
    