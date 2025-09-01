N, M = map(int, input().split())

oro=[]
opciones=[]
result=[0]*(N+1)
op1=0
opcion1=0
opcion2=0

for i in range(M):
    a = list(map(int, input().split()))
    
    oro.append(a)
    
    a = list(map(int, input().split()))
    
    opciones.append(a)



for x in range(M):
    
    for y in range(N):
        if (opciones[x][y])==1:
            op1+=1
        
    opcion1=oro[x][0]//(op1+1)
    opcion2=oro[x][1]
        
    if opcion1<opcion2:
        result[N]+=opcion2
        if op1>0:
            opcion1=oro[x][0]//op1
    else:
        result[N]+=opcion1
            
    for k in range(N):
        if (opciones[x][k])==1:
            result[k]+=opcion1
        else:
            result[k]+=opcion2
            
    op1=0
    
            
            
print(" ".join(map(str, result)))