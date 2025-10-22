N, M = map(int, input().split())
A = list(map(int, input().split()))
E = list(map(int, input().split()))
salida = []
calculados = {}

for alfajores in A:
    if alfajores in calculados:
        salida.append(calculados[alfajores])
        continue
    alfajoresactuales = alfajores
    for x in E:
        if alfajoresactuales < x:
            continue
        if x == 1:
            alfajoresactuales = 0
            break
        else:
            alfajoresactuales %= x
        if alfajoresactuales == 0:
            break
    calculados[alfajores] = alfajoresactuales
    salida.append(alfajoresactuales)    

print(" ".join(map(str, salida)))