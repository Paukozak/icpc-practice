B = input().strip()
S = int(input())
n = len(B)

# Si no hay ninguna 'E', el resultado es 0
if 'E' not in B:
    print(0)
else:
    # Hacemos la cadena doble para simular circularidad
    B2 = B + B

    # Lista para almacenar la distancia al próximo 'E' desde cada posición
    nextEdist = [0] * (2 * n)
    distancia = 10**9  # valor grande inicial

    # Recorremos la cadena desde el final para calcular la distancia
    for i in range(2 * n - 1, -1, -1): #recorre desde 2*n-1 hasta 0 y va restando 1
        if B2[i] == 'E':
            distancia = 0  # encontramos una 'E'
        else:
            distancia += 1  # aumentamos la distancia
        nextEdist[i] = distancia

    # Calculamos la suma total considerando el mínimo entre S y la distancia
    total_allP = 0
    for i in range(n):
        total_allP += min(S, nextEdist[i])

    # Resultado final
    ans = n * S - total_allP
    print(ans)
