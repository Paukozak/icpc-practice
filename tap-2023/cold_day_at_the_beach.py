import math
import heapq

N = int(input()) #Cantidad de lanzamientos
W, L, Tx, Ty = map(int, input().split()) #Ancho, Largo, Tejin en x, Tejin en y
distanciasA = []
distanciasR = []

for x in range(N):
    entx, enty = map(int, input().split())
    suma = ((Tx-entx)**2)+((Ty-enty)**2)
    heapq.heappush(distanciasA, math.sqrt(suma)) 

for x in range(N):
    entx, enty = map(int, input().split())
    suma = ((Tx-entx)**2)+((Ty-enty)**2)
    heapq.heappush(distanciasR, math.sqrt(suma)) 

puntos = 0
i=0

if distanciasA[0] < distanciasR[0]:
    ganador = 'A'
    while distanciasA[i] < distanciasR[0] and i < N:
        puntos+= 1
        i+=1
else:
    ganador = 'B'
    while distanciasR[i] < distanciasA[0] and i < N:
        puntos+= 1
        i+=1

print(ganador, puntos)