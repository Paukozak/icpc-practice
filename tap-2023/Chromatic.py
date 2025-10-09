N=int(input())

amigas=list(map(int, input().split()))
tarros2=list(map(int, input().split()))

amigas.sort(reverse=True)
tarros2.sort()

for i in range(N):
    amigas[i]+=tarros2[i]

menor=min(amigas)
mayor=max(amigas)

print(mayor-menor)
    

