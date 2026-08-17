largo, cant_partidas = map(int, input().split())
n=list(map(int, input().split()))
result=[]
pref_imp=[0]
pref_p2=[0]
pref_unos=[0]

def es_potencia_de_2(n):
    return (n & (n - 1)) == 0

for num in n:
    if num==1:
        pref_unos.append(pref_unos[-1]+num)
        pref_imp.append(pref_imp[-1])
        pref_p2.append(pref_p2[-1])
    elif num % 2 == 1:
        pref_unos.append(pref_unos[-1])
        pref_imp.append(pref_imp[-1]+num)
        pref_p2.append(pref_p2[-1])
    elif es_potencia_de_2(num) == True:
        pref_unos.append(pref_unos[-1])    
        pref_p2.append(pref_p2[-1]+num)
        pref_imp.append(pref_imp[-1])
    else:
        pref_p2.append(pref_p2[-1])
        pref_imp.append(pref_imp[-1])
        pref_unos.append(pref_unos[-1])

#print (pref_unos)
#print(pref_p2)
#print(pref_imp)    

for i in range(cant_partidas):
    rango=list(map(int, input().split()))
    inicio=rango[0]-1
    fin=rango[1]
    a=0
    b=0
    #sublista=n[inicio:fin]
    p2=[]
    imp=[]
    unos=[]
    
    #print(sublista)
    
    #unos=sublista.count(1)
    #if unos % 2 == 1:
    #    a+=1
        
     
    #print("Puntos a: ",(pref_p2[fin]-pref_p2[inicio])+a)
    #print("Puntos b: ",pref_imp[fin]-pref_imp[inicio])
    if (pref_unos[fin]-pref_unos[inicio])%2==1:
        a+=1

    if (pref_imp[fin]-pref_imp[inicio])>((pref_p2[fin]-pref_p2[inicio])+a):
        result.append("B")
    elif (pref_imp[fin]-pref_imp[inicio])<((pref_p2[fin]-pref_p2[inicio])+a):
        result.append("A")
    else:
        result.append("E")
    # for num in sublista:
    #     if num==1:
    #         unos.append(1)
    #     elif num % 2 == 1:
    #         imp.append(num)
    #     elif es_potencia_de_2(num) == True:
    #         p2.append(num)
            
    # a=sum(p2)
    # b=sum(imp)
    
    # if len(unos) % 2 == 1:
    #     a+=1
    
    # if a>b:
    #     result.append("A")
    #     #print("A")
    # elif b>a:
    #     result.append("B")
    #     #print("B")
    # else:
    #     result.append("E")
    #     #print("E")
        
print(" ".join(map(str, result))) 