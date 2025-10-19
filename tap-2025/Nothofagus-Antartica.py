N=int(input())
C=[]
mayorX=0
mayorY=0
menorX=1000000000
menorY=1000000000

for i in range(N):
    a = list(map(int, input().split()))
    C.append(a)
    if a[0]>mayorX:
       mayorX=a[0]
    if a[1]>mayorY:
       mayorY=a[1] 
    if a[0]<menorX:
       menorX=a[0]
    if a[1]<menorY:
       menorY=a[1]

per=((mayorX-menorX+2)*2+(mayorY-menorY+2)*2)

print(per)