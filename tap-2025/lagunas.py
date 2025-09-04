N, G = map(int, input().split())
T = list(map(int, input().split()))
cantbarcos = 0
resta = N
i = 1
bandera = True
while bandera:
    if resta-i >= 0:
        cantbarcos+=1
        resta-= i
        i+= 1
    else:
        bandera = False


tabla = [[0]*(N+1) for _ in range(cantbarcos+1)]

def calcular(inicio, fin):
    if inicio == 1: #Estoy en la primer fila (1 barco)
        if G - T[fin-1] > 0: # Si saco ganancia cavando en esa posicion
            if tabla[inicio][fin-1] < G - T[fin-1]: # Pone el actual porque es mayor que el de antes 
                tabla[inicio][fin] = G - T[fin-1]
            else: # Sino si el que esta antes es mayor que el posible actual, pone el de antes
                tabla[inicio][fin] = tabla[inicio][fin-1]
        else: # No saco ganancia, me quedo con el anterior
            tabla[inicio][fin] = tabla[inicio][fin-1]
    elif inicio > fin-1:
        tabla[inicio][fin] = tabla[inicio-1][N]
    else: #Esta en la segunda fila en adelante
        porcion = T[fin-inicio:fin]
        print(porcion)
        if G - sum(porcion) > 0:
            if tabla[inicio][fin-1] < G - sum(porcion) + tabla[inicio-1][fin]: # Pone el actual y le suma el de antes porque es mayor que el de antes 
                tabla[inicio][fin] = G - sum(porcion) + tabla[inicio-1][fin]
            else: # Sino si el que esta antes es mayor que el posible actual, pone el de antes
                tabla[inicio][fin] = tabla[inicio][fin-1]
        else: # No saco ganancia, me quedo con el anterior
            tabla[inicio][fin] = tabla[inicio][fin-1]
    

for i in range(1, cantbarcos + 1):  # para cada cantidad de barcos
    for j in range(1, N + 1):  # para cada posición
        calcular(i, j)
        
# La respuesta está en tabla[cantbarcos][N]
print(tabla)