n, x = map(int, input().split())
b = list(map(int, input().split()))

b.sort(reverse=True)  # Ordenamos de mayor a menor

res = []
count = {}

# Contamos la cantidad de cada belleza
for val in b:
    count[val] = count.get(val, 0) + 1

# Lista de resultados
res = []

# Ordenamos de menor a mayor
b.sort()

i = 0
j = n - 1
ok = True
res = []

while i <= j:
    # Elegimos el más grande disponible
    if not res:
        res.append(b[j])
        j -= 1
    else:
        if res[-1] + b[i] != x:
            res.append(b[i])
            i += 1
        elif res[-1] + b[j] != x:
            res.append(b[j])
            j -= 1
        else:
            ok = False
            break

if ok:
    print(*res)
else:
    print("*")
