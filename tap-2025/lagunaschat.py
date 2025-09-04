N, G = map(int, input().split())
T = list(map(int, input().split()))

# Precalcular sumas parciales para calcular costos en O(1)
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + T[i]

# dp[barcos][pos] = máxima ganancia con barcos barcos, 
# donde el último barco termina en la posición pos
dp = [[-float('inf')] * (N + 1) for _ in range(N + 1)]
# mejor_longitud[barcos][pos] = longitud del último barco en la solución óptima
mejor_longitud = [[0] * (N + 1) for _ in range(N + 1)]

# Caso base: 0 barcos, 0 ganancia para todas las posiciones
for j in range(N + 1):
    dp[0][j] = 0

for barcos in range(1, N + 1):
    for pos in range(N + 1):
        # Propagar el resultado sin colocar barco en esta posición
        if pos > 0:
            dp[barcos][pos] = dp[barcos][pos-1]
            mejor_longitud[barcos][pos] = mejor_longitud[barcos][pos-1]
        
        # Intentar colocar un barco que termina en 'pos'
        for longitud in range(1, pos + 1):
            inicio = pos - longitud
            
            # Calcular el costo de excavación
            costo = prefix_sum[pos] - prefix_sum[inicio]
            ganancia = G - costo
            
            if ganancia <= 0:  # No es rentable
                continue
            
            for prev_pos in range(inicio + 1):
                if dp[barcos-1][prev_pos] == -float('inf'):
                    continue
                
                prev_longitud = mejor_longitud[barcos-1][prev_pos]
                
                # Verificar que las longitudes sean estrictamente crecientes
                if prev_longitud >= longitud and prev_longitud > 0:
                    continue
                
                nueva_ganancia = dp[barcos-1][prev_pos] + ganancia
                
                if nueva_ganancia > dp[barcos][pos]:
                    dp[barcos][pos] = nueva_ganancia
                    mejor_longitud[barcos][pos] = longitud

# Encontrar la máxima ganancia
resultado = max(dp[i][N] for i in range(N + 1))
print(resultado)