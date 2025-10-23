largo, cant_partidas = map(int, input().split())
n=list(map(int, input().split()))
result=[]

def es_potencia_de_2(n):
    return n > 0 and (n & (n - 1)) == 0

for i in range(cant_partidas):
    rango=list(map(int, input().split()))
    inicio=rango[0]-1
    fin=rango[1]
    
    sublista=n[inicio:fin]
    p2=[]
    imp=[]
    
    for num in sublista:
        if num % 2 == 1:
            imp.append(num)
        
        if es_potencia_de_2(num) == True:
            p2.append(num)
            
    t=0
    ag=0
    br=0
    agpass=0
    brpass=0
    
    while len(sublista)>0 and (agpass<2 and brpass<2):
        if 1 in sublista:
            sublista.remove(1)
            p2.remove(1)
            imp.remove(1)
            if t==0:
                ag+=1
            else:
                br+=1
        else:
            if t==0:
                if (len(p2)>0):
                    valor=max(p2)
                    ag+=valor
                    p2.remove(valor)
                    sublista.remove(valor)     
                else:
                    agpass+=1
            else:
                if (len(imp)>0):
                    valor=max(imp)
                    br+=valor
                    imp.remove(valor)
                    sublista.remove(valor)     
                else:
                    brpass+=1 
            
        #print("turno: ",t)
        #print("agustin: ",ag)
        #print("brian: ",br)
        #print("sublista: ",sublista)
        #print("paso-ag: ",agpass)
        #print("paso-br: ",brpass) 
            
        t^=1
        
    if ag>br:
        result.append("A")
        #print("A")
    elif br>ag:
        result.append("B")
        #print("B")
    else:
        result.append("E")
        #print("E")

print(" ".join(map(str, result))) 
