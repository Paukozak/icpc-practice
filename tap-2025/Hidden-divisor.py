#!/usr/bin/env python3
import sys
import math
import random

# Constante límite usada para protegerse contra overflow/valores muy grandes.
# Representa un tope razonable para este problema (10^18).
MAXX = 10**18

def is_prime(n: int) -> bool:
    # Test de primalidad fuerte y rápido.
    # - Eliminamos casos triviales (< 2)
    # - Probamos división por un pequeño conjunto de primos para filtrar rápidos
    # - Aplicamos Miller-Rabin con bases deterministas válidas para enteros <= 2^64
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            # si es divisible por p, es primo sólo si n == p
            return n == p
    # Escribimos n-1 como d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Conjunto de bases deterministas suficiente para 64-bit
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True

def pollards_rho(n: int) -> int:
    # Algoritmo de Pollard's Rho para encontrar un factor no trivial de n.
    # Manejo rápido de factores pequeños
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    # Intentamos con polinomio aleatorio f(x) = x^2 + c
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            # avance tortuga (x) y liebre (y) con el mismo polinomio
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
            if d == n:
                # fracaso en este intento, probamos nuevos parámetros
                break
        if d > 1 and d < n:
            return d

def factor(n: int, res: dict):
    # Factorización recursiva: llena el diccionario 'res' con {prime: exponent}
    if n == 1:
        return
    if is_prime(n):
        res[n] = res.get(n, 0) + 1
        return
    d = pollards_rho(n)
    # Factorizamos el divisor encontrado y el cociente
    factor(d, res)
    factor(n // d, res)

def safe_lcm(a: int, b: int) -> int:
    # Calcula el mcm de a y b con comprobación de overflow respecto a MAXX.
    # Si el resultado excede MAXX devolvemos MAXX+1 como señal de desborde.
    g = math.gcd(a, b)
    a_div = a // g
    if a_div != 0 and b > MAXX // a_div:
        return MAXX + 1
    return a_div * b

def gen_divisors_from_factors(factors: list):
    # Genera todos los divisores a partir de la lista de factores
    # factors: lista de tuplas (prime, exponent)
    divisors = [1]
    for p, e in factors:
        cur = []
        mul = 1
        # Para cada potencia p^k (k=0..e) multiplicamos los divisores previos
        for k in range(e + 1):
            for d in divisors:
                cur.append(d * mul)
            mul *= p
        divisors = cur
    return divisors

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    s = set(arr)
    # duplicates are invalid
    if len(s) != n:
        # Si hay duplicados, entrada inválida -> imprimir '*' siguiendo especificación
        print("*")
        return
    # compute lcm
    L = 1
    for a in arr:
        L = safe_lcm(L, a)
        if L > MAXX:
            # Si el LCM se desborda el límite, no hay solución válida
            print("*")
            return
    # every a must divide L
    for a in arr:
        if L % a != 0:
            # Si algún a no divide el L encontrado, entrada inconsistente
            print("*")
            return
    # factor L
    factors = {}
    factor(L, factors)
    # target number of divisors
    target_tau = n + 1

    # list of existing primes and their exponents in L
    fac_list = sorted(factors.items())
    primes = [p for p, e in fac_list]
    el = [e for p, e in fac_list]

    # get divisors of target_tau
    def divisors(x):
        ds = []
        i = 1
        while i * i <= x:
            if x % i == 0:
                ds.append(i)
                if i != x // i:
                    ds.append(x//i)
            i += 1
        ds.sort()
        return ds

    D = divisors(target_tau)

    # choices for each existing prime: possible values for (ei+1)
    choices = []
    for e in el:
        low = e + 1
        ch = [d for d in D if d >= low]
        if not ch:
            # No es posible aumentar exponentes de los primos existentes para alcanzar tau objetivo
            print("*")
            return
        choices.append(ch)

    candidates = set()

    # backtrack assignments of di for existing primes such that product(di) == target_tau
    m = len(primes)

    def dfs(i, prod, exps):
        if i == m:
            if prod != target_tau:
                return
            # build candidate X
            X = 1
            for idx, p in enumerate(primes):
                di = exps[idx]
                ei = di - 1
                # multiply X by p**ei with overflow check
                if ei > 0:
                    # fast pow with limit
                    val = pow(p, ei)
                    if val > 0 and X > MAXX // val:
                        return
                    X *= val
            if X <= 0 or X > MAXX:
                return
            # ensure all arr divide X
            for a in arr:
                if X % a != 0:
                    return
            # ensure number of divisors equals target_tau
            # compute divisors count of X from exps
            # exps list corresponds to ei+1 already
            tau_calc = 1
            for di in exps:
                tau_calc *= di
            if tau_calc != target_tau:
                return
            candidates.add(X)
            return
        # early prune: prod must divide target_tau
        for d in choices[i]:
            if prod * d > target_tau:
                break
            if target_tau % (prod * d) != 0 and i != m-1:
                # still could be completed by future choices? Actually we require final product equals target_tau,
                # so intermediate product must divide target_tau.
                continue
            exps.append(d)
            dfs(i+1, prod * d, exps)
            exps.pop()

    dfs(0, 1, [])

    if len(candidates) != 1:
        # Debe existir exactamente un candidato X que cumpla todas las condiciones
        print("*")
        return

    X = candidates.pop()
    # generate divisors of X and find missing
    # factor X (we can reuse factors list but exponents may have increased)
    factorsX = {}
    factor(X, factorsX)
    fac_list_X = sorted(factorsX.items())
    divs = gen_divisors_from_factors(fac_list_X)
    ds = set(divs)
    if not s.issubset(ds):
        # Si alguno de los elementos de entrada no es divisor de X -> inválido
        print("*")
        return
    missing = list(ds - s)
    if len(missing) != 1:
        # Debe faltar exactamente un divisor respecto al conjunto de divisores de X
        print("*")
        return
    miss = missing[0]
    print(f"{X} {miss}")

if __name__ == '__main__':
    main()
