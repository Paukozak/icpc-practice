N, M = map(int, input().split())
A = list(map(int, input().split()))
E = list(map(int, input().split()))
final=[]
dic={}
 
for i in range(N):
    
    if (A[i]) in dic:
        final.append(dic[A[i]])
    else:
        inicio=A[i]
        for j in range(M):
            
            if (E[j]<=A[i]):
                div=A[i]//E[j]
                A[i]=A[i]-(E[j]*div)
                            
        final.append(A[i])
        dic[inicio]=A[i]
 
print(" ".join(map(str, final)))