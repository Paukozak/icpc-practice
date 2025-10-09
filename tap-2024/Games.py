# Función auxiliar para determinar si un número es potencia de 2 (bit trick O(1))
def is_power_of_two(x):
    return x != 0 and (x & (x - 1)) == 0

# Leer inputs
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Leemos todas las queries de una vez
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Preprocesado por prefijos: contar/sumar ones, potencias>1 y impares>1
n = N
pref_ones = [0] * (n + 1)
pref_cnt_p2 = [0] * (n + 1)
pref_sum_p2 = [0] * (n + 1)
pref_cnt_odd = [0] * (n + 1)
pref_sum_odd = [0] * (n + 1)

for i, val in enumerate(A):
    pref_ones[i+1] = pref_ones[i] + (1 if val == 1 else 0)

    if val > 1 and is_power_of_two(val):
        pref_cnt_p2[i+1] = pref_cnt_p2[i] + 1
        pref_sum_p2[i+1] = pref_sum_p2[i] + val
    else:
        pref_cnt_p2[i+1] = pref_cnt_p2[i]
        pref_sum_p2[i+1] = pref_sum_p2[i]

    if val > 1 and (val % 2 == 1):
        pref_cnt_odd[i+1] = pref_cnt_odd[i] + 1
        pref_sum_odd[i+1] = pref_sum_odd[i] + val
    else:
        pref_cnt_odd[i+1] = pref_cnt_odd[i]
        pref_sum_odd[i+1] = pref_sum_odd[i]

def play_game(queries):
    results = []
    for L, R in queries:
        # rangos en prefijos (1-indexed)
        ones = pref_ones[R] - pref_ones[L-1]
        cnt_p2 = pref_cnt_p2[R] - pref_cnt_p2[L-1]      # a
        sum_p2 = pref_sum_p2[R] - pref_sum_p2[L-1]      # sA (potencias>1)
        cnt_odd = pref_cnt_odd[R] - pref_cnt_odd[L-1]   # b
        sum_odd = pref_sum_odd[R] - pref_sum_odd[L-1]   # sB (impares>1)

        # Pelea por los '1': se alternan, empezando por Agustín
        ones_A = (ones + 1) // 2
        ones_B = ones // 2

        score_a = sum_p2 + ones_A
        score_b = sum_odd + ones_B

        if score_a > score_b:
            results.append("A")
        elif score_b > score_a:
            results.append("B")
        else:
            results.append("E")
    return results

# Procesamos todas las rondas y mostramos resultados
for res in play_game(queries):
    print(res)