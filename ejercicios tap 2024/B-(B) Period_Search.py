N = int(input().strip())

# Factorización por prueba hasta sqrt(N) para obtener primos distintos (técnica: teoría de números)
primes = []
n = N
d = 2
while d * d <= n:
    if n % d == 0:
        primes.append(d)           # guardamos el primo distinto
        while n % d == 0:
            n //= d                # eliminamos todas las potencias de d
    d += 1 if d == 2 else 2       # incremento simple (salta pares después de 2) - suficiente para N <= 1e6
if n > 1:
    primes.append(n)               # el resto es primo

K = len(primes)                    # número mínimo de preguntas = cantidad de primos distintos
print(K)
# Construimos las preguntas: para cada primo p preguntamos L=1, R=N//p (longitud = N//p)
# (cualquier subsegmento de esa longitud sirve; usamos el inicial por simplicidad)
for p in primes:
    length = N // p
    print(1, length)