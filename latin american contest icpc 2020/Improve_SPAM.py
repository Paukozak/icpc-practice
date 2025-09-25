#ddv: []

def recorrer(num_ml):
    global ddv
    
    lista_ml=dic_entrada[num_ml]
    #lista_ml=[4, 5]
    for z in range(len(lista_ml)):
        if lista_ml[z] <= L and lista_ml[z] not in ddv: #es un mailing list
            ddv.append(lista_ml[z])
            recorrer(lista_ml[z])
    
        elif lista_ml[z] > L: #es un mail directo
            if lista_ml[z] in dic_salida:
                dic_salida[lista_ml[z]]+=1
            else:
                dic_salida[lista_ml[z]]=1
    
    del lista_ml[len(lista_ml)-1]

N, L= map(int,input().split())
dic_entrada={}
dic_salida={}
ddv=[]

for i in range(1,L+1):
    l=list(map(int,input().split()))
    dic_entrada[i]=[]
    for j in range(l[0]):        
        dic_entrada[i].append(l[j+1])

finished=False

ddv.append(1)
recorrer(1)

r1=sum(dic_salida.values())
r2=len(dic_salida)

print(r1, r2)