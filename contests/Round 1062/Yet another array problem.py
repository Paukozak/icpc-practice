import math # math.gcd(num1, num2): Devuelve el máximo común divisor de dos números.
t = int(input())
for i in range(t):
    n = int(input())
    arreglo = list(map(int, input().split()))
    x = 2
    mcd = 0
    while x <= (10**18) and mcd != 1:
        for j in range(n):
            mcd = math.gcd(x, arreglo[j])
            if mcd == 1:
                break
        x+=1
    if mcd == 1:
        print(x-1)
    else:
        print(-1)

