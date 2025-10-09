# Leemos el número de valores posibles
N = int(input())

# Leemos la lista de dimensiones permitidas
values = list(map(int, input().split()))

# Encontramos el valor mínimo y el valor máximo de la lista
minV = min(values)
maxV = max(values)

# Aplicamos la fórmula deducida:
# La máxima ganancia es (maxV - minV)^2
profit = (maxV - minV) ** 2

# Imprimimos el resultado
print(profit)
