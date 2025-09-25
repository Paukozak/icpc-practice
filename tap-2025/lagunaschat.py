N, G = map(int, input().split())
T = list(map(int, input().split()))

# Precalcular sumas parciales para calcular costos en O(1)
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + T[i]

# Fast path: if all cells are water (all Ti == 0), then every boat of any length
# gives profit G and the only constraint is sum of distinct increasing lengths <= N.
# Maximum number of boats m satisfies m*(m+1)/2 <= N. Answer = m * G.
if all(x == 0 for x in T):
    # solve m*(m+1)/2 <= N -> m = floor((sqrt(8N+1)-1)/2)
    import math
    m = int((math.isqrt(8 * N + 1) - 1) // 2)
    print(m * G)
    raise SystemExit

NEG_INF = -10**18

# best[i] = mejor ganancia hasta la posición i usando barcos de longitud < L (para la iteración actual)
best = [0] * (N + 1)

for L in range(1, N + 1):
    # cur[pos] = mejor ganancia hasta pos permitiendo exactamente longitudes <= L
    cur = [NEG_INF] * (N + 1)
    cur[0] = 0

    for pos in range(1, N + 1):
        # Propagar sin colocar barco que termine en pos
        cur[pos] = cur[pos - 1]

        if pos >= L:
            start = pos - L
            costo = prefix_sum[pos] - prefix_sum[start]
            ganancia = G - costo
            if ganancia > 0:
                cand = best[start] + ganancia
                if cand > cur[pos]:
                    cur[pos] = cand

    # Actualizar 'best' para permitir ahora longitudes <= L en futuras iteraciones
    for i in range(N + 1):
        if cur[i] > best[i]:
            best[i] = cur[i]

print(max(best))