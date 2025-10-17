import sys
input = sys.stdin.readline

# Leer entrada
N, M = map(int, input().split())
A = list(map(int, input().split()))
E = list(map(int, input().split()))

# Filtrar solo los mínimos estrictos (prefijos que realmente reducen)
S = []
min_so_far = float('inf')
for e in E:
    if e < min_so_far:
        S.append(e)
        min_so_far = e

# Resolver para cada viaje
ans = []
cache = {}

for a in A:
    if a in cache:
        ans.append(cache[a])
        continue
    r = a
    for e in S:
        r %= e
    cache[a] = r
    ans.append(r)

# Imprimir resultado
print(" ".join(map(str, ans)))