def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        tabla = [0] * (n+1)
        tabla[1] = 1
        for x in range(1, delay+1):
            tabla[x] = 1

        for i in range(delay, n+1):
            tabla[i] = tabla[i-1] 
            if i % forget+1 == 0:
                tabla[i] -= tabla[i-forget]
            tabla[i] += tabla[i-delay]
        print(tabla)
        return tabla[n] % (1000000000+7)