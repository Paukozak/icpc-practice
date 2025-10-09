# Final Showdown - solución DP 0/1 sobre potencia (sin imports)

INF_NEG = -10**18  # -inf para el DP

# Leer entrada
N, P = map(int, input().split())
weapons = [tuple(map(int, input().split())) for _ in range(N)]  # (A, B, C)

# dp[p] = máximo daño alcanzable estando con potencia p tras procesar un conjunto de armas
# inicial: sólo estado alcanzable es potencia inicial P con daño 0
dp = [INF_NEG] * (P + 1)
dp[P] = 0

# Técnica central: procesar cada arma como item 0/1.
# Para cada arma (A,B,C) usamos una copia old = dp (estados sin usar esa arma),
# y actualizamos new_dp considerando usar o no usar la arma.
for (A, B, C) in weapons:
    old = dp[:]                  # old: dp antes de usar la arma (garantiza 0/1)
    # no usar arma: new starts as old (ya lo está)
    # usar arma: para cada potencia p desde B..P con old[p] válido:
    #   new_p = floor((p - B) / A)
    #   new_dp[new_p] = max(new_dp[new_p], old[p] + C)
    for p in range(B, P + 1):
        val = old[p]
        if val == INF_NEG:
            continue
        new_p = (p - B) // A
        # new_p está en rango 0..p (puede ser 0)
        if dp[new_p] < val + C:
            dp[new_p] = val + C

# Tras procesar todas las armas, la respuesta V es el máximo daño alcanzable en cualquier potencia >= 0
answer = max(dp)
if answer < 0:
    # si no se puede hacer daño (aunque 0 es posible), devolver 0
    answer = 0
print(answer)