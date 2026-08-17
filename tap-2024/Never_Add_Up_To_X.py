n, x = map(int, input().split())
b = list(map(int, input().split()))

b.sort()  # Ordenamos de menor a mayor
#primero ordeno
#creo diccionario para saber cuantos valores hacia adelante cambiar (ya que voy a ver de izq a derecha)
#y mando
perm={}

for beauty in b:
    if beauty not in perm: 
        perm[beauty]=1
    else:
        perm[beauty]+=1

if n==2:
    if (b[0]+b[1])==x:
        print ('*')
    else:
        print (" ".join(map(str, b)))
else:
    for i in range(len(b)-1):
        aux=b[i]+b[i+1]
        if aux==x:
            if (i-(perm[b[i]]))>=0:
                aux=b[i]
                temp=b[i]
                b[i]=b[i-perm[b[i]]]
                b[i-perm[temp]]=aux
                print (" ".join(map(str, b)))
                break
            elif (i+1+perm[b[i+1]])<=(len(b)-1):
                aux=b[i+1]
                temp=b[i+1]
                b[i+1]=b[i+1+perm[b[i+1]]]
                b[i+1+perm[temp]]=aux
                print (" ".join(map(str, b)))
                break
            else:
                print('*')
                break
        elif i==(len(b)-2):
            print (" ".join(map(str, b)))





