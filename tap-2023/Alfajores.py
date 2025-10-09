N, M = map(int, input().split())
A = list(map(int, input().split()))
E = list(map(int, input().split()))

final = []

for alfajores in A:
    sobrante = alfajores
    for empleados in E:
        sobrante %= empleados 
    final.append(sobrante)

print(" ".join(map(str, final)))
