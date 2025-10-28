n=int(input())
impares=[]
pares=[]


for i in range(n):
    a=int(input())
    arr=list(map(int, input().split()))
    
    for num in arr:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    pares.sort()
    impares.sort()
    i=0
    j=0

    while i<len(pares) and j<len(impares):
        print(i)
        print(j)

        ind_p=arr.index(pares[i])
        ind_j=arr.index(impares[j])
            
        print(ind_p)
        print(ind_j)
            
        print(arr) 
        if (pares[i]>impares[j]) and (ind_j>ind_p):
            aux=arr.pop(ind_p)
            print(arr) 
            arr.insert(ind_j,aux)
            print(arr)
            ind_j=arr.index(impares[j])
            aux=arr.pop(ind_j)
            print(arr) 
            arr.insert(ind_p,aux)  
            
            print(arr)   
        
            j+=1   
        else:
            
            if (pares[i]<impares[j]) and (ind_j<ind_p):
                aux=arr.pop(ind_p)
                print(arr) 
                arr.insert(ind_j,aux)
                print(arr)
                ind_j=arr.index(impares[j])
                aux=arr.pop(ind_j)
                print(arr) 
                arr.insert(ind_p,aux)  
                
                print(arr)   
            
            i+=1 

    print(arr)
