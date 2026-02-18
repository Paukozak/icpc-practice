n=int(input())
results=[]

for i in range(n):
    a=int(input())
    arr=list(map(int, input().split()))
    p=0
    i=0
    
    for num in arr:
        if num % 2 == 0:
            p+=1
        else:
            i+=1
    
    if p>0 and i>0:
        arr.sort()

    results.append(arr)
    
for lista in results:
    print(" ".join(map(str, lista))) 
