# L. Lakes — DP con prefijos y mínimos prefix (O(N * k_max))
# Técnica principal: Programación Dinámica con prefijos y mínimo prefijo incremental.
# Idea: colocar k barcos de longitudes 1..k en orden izquierda->derecha equivale a elegir
# k segmentos disjuntos [r_j - L_j + 1, r_j], r_1 < r_2 < ... < r_k, que minimicen el costo
# de excavar (suma de Ti>0 dentro de cada segmento). El costo de un segmento [l..r] es
# W[r] - W[l-1], donde W es el prefijo de costos positivos.
# DP: dp_j[r] = costo mínimo para ubicar j barcos y que el j-ésimo termine en r.
# Transición: dp_j[r] = (W[r] - W[r-L_j]) + min_{t <= r - L_j} dp_{j-1}[t].
# El término min_{t <= x} es un mínimo prefijo que se mantiene incrementalmente en O(1) por r.
# Complejidad: O(N * k_max), donde k_max = floor((sqrt(8N+1)-1)/2) ~ 447 para N=1e5. En Python
# es ajustado pero factible con bucles apretados y sin estructuras pesadas.

import sys, math

def solve():
    input = sys.stdin.readline

    # --- Lectura ---
    N, G = map(int, input().split())
    T = list(map(int, input().split()))

    # --- Costos positivos (agua=0) ---
    # C[i] es el costo de excavar la celda i si fuera tierra (0 si ya es agua)
    C = [0] * N
    for i, x in enumerate(T):
        if x > 0:
            C[i] = x

    # --- Prefijos de costo: W[i] = suma C[0..i-1] ---
    W = [0] * (N + 1)
    s = 0
    for i in range(N):
        s += C[i]
        W[i + 1] = s

    # --- Máximo número de barcos que pueden caber por longitud total S = k(k+1)/2 <= N ---
    k_max = (math.isqrt(8 * N + 1) - 1) // 2

    # --- DP base: dp_0[r] = 0 (costo de colocar 0 barcos y terminar en r) ---
    INF = 10**19
    prev = [0] * (N + 1)

    ans = 0

    # --- Bucle por cantidad de barcos j = 1..k_max ---
    for j in range(1, k_max + 1):
        L = j  # longitud del j-ésimo barco
        dp = [INF] * (N + 1)

        # Mantendremos el mínimo prefijo de prev[0..r-L] en 'curr_min'
        curr_min = prev[0]
        best = INF  # mejor costo para exactamente j barcos

        # Locales para acelerar accesos en el bucle apretado
        Wloc = W
        prevloc = prev

        # r recorre las posiciones posibles de final del j-ésimo barco (r >= L)
        for r in range(L, N + 1):
            v = prevloc[r - L]
            if v < curr_min:
                curr_min = v  # curr_min = min(prev[0..r-L])

            # costo de excavar el segmento [r-L+1 .. r]
            cost_seg = Wloc[r] - Wloc[r - L]
            val = cost_seg + curr_min
            dp[r] = val
            if val < best:
                best = val

        # Actualizamos la mejor ganancia neta con j barcos
        gain = j * G - best
        if gain > ans:
            ans = gain

        # dp_j pasa a ser prev para la próxima iteración
        prev = dp

    # Opción de no colocar barcos (ganancia 0)
    if ans < 0:
        ans = 0

    print(ans)

solve()
