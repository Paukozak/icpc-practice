N=int(input())
r=list(map(int, input().split())) 
b=list(map(int, input().split()))

r.sort()
b.sort(reverse=True)
#print (r)
#print (b)
result=[]

for i in range (N):
    valor=r[i]+b[i]
    result.append(valor)

result.sort()
#print(result)
mayor=result[0]
menor=result[N-1]

print(abs(mayor-menor))
