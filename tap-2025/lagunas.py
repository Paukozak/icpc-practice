N, G = map(int, input().split())
T = list(map(int, input().split()))
cantbarcos = 0
resta = N
i = 1
cantbarcos=0
cont=0

while resta>0:
    cantbarcos+=1
    resta-=cantbarcos
    

gananciatotal = 0

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
    cont+=i
    for j in range(1, N + 1):  # para cada posición
        # Opción 1: no colocar barco en la posición j
        
        if j>1:
            tabla[i][j] = tabla[i][j-1]
        else:
            tabla[i][j]=tabla[i-1][N]

        #print("1) en la fila ",i," columna ",j," puse ",tabla[i][j])
  
        # Opción 2: colocar el i-ésimo barco terminando en la posición j
        # El barco i tiene longitud i
        if j >= cont:  # si hay suficiente espacio
            costo_excavacion = calcular_costo(j-i, j)  # costo de excavar desde j-i hasta j
            ganancia_neta = G - costo_excavacion
            
            #print("hay espacio")
            #print("ganancia: ", ganancia_neta)

            if ganancia_neta > 0:  # cambié > por >= para incluir ganancias de 0
                if i == 1:
                    tabla[i][j] = max(tabla[i][j], ganancia_neta)
                else:
                    tabla[i][j] = max(tabla[i][j], tabla[i-1][j-i] + ganancia_neta)
                

            #print("cambie el valor por: ",tabla[i][j])

# La respuesta está en taaaaklkjkjrcos][N]
print(tabla[cantbarcos][N])