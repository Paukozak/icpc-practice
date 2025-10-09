N, X = map(int, input().split())
#K = [float(x) for x in input().split()]
K = list(map(int, input().split()))

K.sort()
#E = []
#E.append(K[0])
#K.pop(0)
#i = 0
#e = 0

if N == 2 and K[0] + K[1] == X:
    print("*")
else:
    for i in range(N - 1):
        if K[i] + K[i + 1] == X:
            K = K[i + 1:] + K[:i + 1] #esto es una rotación de lista 
            break
    print(" ".join(map(str, K)))   
    
    
#explicacion de la rotacion
#vos tenes una lista 1 2 2 3 4
# i = 3 entonces K[i]=2
#agarra los valores desde i hasta el final 
#y por otro lado desde el inicio hasta i
#y los cambia de lugar
#la lista queda: 3 4 1 2 2






#while len(K) != 0:
#    if ((K[i] + E[e]) != X): 
#        e+=1
#        E.insert(e,K[i])
#        K.pop(i)
#        i = 0
#    elif e==0:
#        i+=1
#    else:
#        e-=1
#        if ((K[i] + E[e]) != X):
#            E.insert(e,K[i])
#            K.pop[i]
#            e+=2


