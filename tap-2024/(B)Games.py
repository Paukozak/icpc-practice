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

    if (pref_unos[fin]-pref_unos[inicio])%2==1:
        a+=1

    if (pref_imp[fin]-pref_imp[inicio])>((pref_p2[fin]-pref_p2[inicio])+a):
        result.append("B")
    elif (pref_imp[fin]-pref_imp[inicio])<((pref_p2[fin]-pref_p2[inicio])+a):
        result.append("A")
    else:
        result.append("E")
        
print(" ".join(map(str, result))) 