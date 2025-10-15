N, M = map(int, input().split())
A = list(map(int, input().split()))
E = list(map(int, input().split()))
salida = []
calculados = {}

for alfajores in A:
    alfajoresactuales = alfajores
    if alfajores in calculados:
        salida.append(calculados[alfajores])
        continue
    for x in E:
        alfajoresactuales = alfajoresactuales % x
        calculados[alfajores] = alfajoresactuales
    salida.append(alfajoresactuales)    

print(" ".join(map(str, salida)))