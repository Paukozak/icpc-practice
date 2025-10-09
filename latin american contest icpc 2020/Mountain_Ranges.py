N, X= map(int,input().split())
A=list(map(int,input().split()))

viewpoints=1
maximo=1

if len(A)==1:
    viewpoints=1
else:
    for i in range (1, len(A)):
        if ((A[i]-A[i-1])<=X):
            viewpoints+=1
            if viewpoints>maximo:
                maximo=viewpoints
        else:
            viewpoints=1

print(maximo)