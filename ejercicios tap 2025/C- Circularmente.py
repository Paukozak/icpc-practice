N=int(input())
P=list(map(int, input().split())) 

cont=0
aux=0
for x in range (N):

    for i in range (N):
        if (i+1)==P[(P[i]-1)]:
            cont+=1
    aux=P[0]
    P.pop(0)
    P.append(aux)

print(cont)
