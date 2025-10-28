# Función auxiliar para determinar si un número es potencia de 2 (bit trick O(1))
def is_power_of_two(x):
    return x != 0 and (x & (x - 1)) == 0

# Leer inputs
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Leemos todas las queries de una vez
queries = [tuple(map(int, input().split())) for _ in range(Q)]