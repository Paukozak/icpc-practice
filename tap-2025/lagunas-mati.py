import math
N, G = map(int, input().split())
T = list(map(int, input().split()))
cantbarcos = 0
resta = N
i = 1
#cantbarcos=1
cont=0

#while resta>=cantbarcos:
 #   resta-=cantbarcos
  #  cantbarcos+=1

#cantbarcos-=1
cantbarcos = int((math.sqrt(1 + 8*N) - 1) // 2)
gananciatotal = 0

tabla = [[0]*(N+1) for _ in range(cantbarcos+1)]

prefix = [0] * (N+1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + T[i - 1]


def calcular_costo(inicio, fin):
    costo = 0
    for k in range(inicio, fin):
      # Si es tierra (no agua)
        costo += T[k]
    return costo
#print(prefix)
for i in range(1, cantbarcos+1):  # para cada cantidad de barcos
    cont+=i
    for j in range(1, N+1):  # para cada posición
        # Opción 1: no colocar barco en la posición j
        costo_excavacion = prefix[j] - prefix[j-i]  # costo de excavar desde j-i hasta j
        ganancia_neta = G - costo_excavacion
        #print(ganancia_neta)
        tabla[i][j]=tabla[i-1][j]
        if j >= cont:
            if ganancia_neta>0:
                if i == 1:
                    tabla[i][j]=max(tabla[i][j-1], ganancia_neta) 
                elif tabla[i][j]<(tabla[i-1][j-i] + ganancia_neta):
                    tabla[i][j]=max(tabla[i-1][j-i] + ganancia_neta,tabla[i][j-1])
            else: 
                tabla[i][j]= max(tabla[i][j-1],tabla[i-1][j])

print(tabla[cantbarcos][N])

print (tabla)
