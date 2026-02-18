t = int(input())
for i in range(t):
    n = int(input())
    arreglo = list(map(int, input().split()))
    haypar = False
    hayimpar = False
    for j in arreglo:
        if j % 2 == 0:
            haypar = True
            continue
        if j % 2 == 1:
            hayimpar = True
    if hayimpar and haypar:
        ordenado = arreglo.sort()
        print(ordenado)
    else:
        print(arreglo)
            