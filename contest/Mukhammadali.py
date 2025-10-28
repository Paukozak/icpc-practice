t=int(input())

for i in range (t):
    n=int(input())
    arr=list(map(int, input().split()))
    cost=list(map(int, input().split()))
    pref_cost=[0]
    for j in range (1,len(cost)):
        pref_cost.append(pref_cost[j-1]+cost[j-1])
    
    matriz = [0 for _ in range(len(arr))]
    
    matriz[0]=0
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            #matriz[i]=min(cost[i]+matriz[i-1],pref_cost[i])
            if cost[i]+matriz[i-1]<pref_cost[i]:
                j=1
                acum=0
                while arr[i]<arr[i-j] and ((i-j)>=0):
                    acum=cost[i-j]+acum 
                    j+=1
                print(acum)
                if acum>=cost[i]:
                    matriz[i]=matriz[i-j]+cost[i]
                    arr[i-1]=arr[i]
                else:
                    matriz[i]=cost[i]+matriz[i-1]
                    arr[i]=arr[i-1]
            else:
                matriz[i]=pref_cost[i]
                
                
        else:
            matriz[i]=matriz[i-1]
            
        
            
    print(arr)
    print(matriz)
    print (matriz[len(arr)-1])
