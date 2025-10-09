MOD = 10**9 + 7

def contar_total(num_ml):
    #Cuenta todos los envíos con duplicados (B)
    if num_ml in memo_total:
        return memo_total[num_ml]

    total = 0
    for destino in dic_entrada[num_ml]:
        if destino <= L:  # mailing list
            total += contar_total(destino)
        else:  # mail directo
            total += 1

    memo_total[num_ml] = total
    return total


def marcar_unicos(num_ml):
    #Marca mails únicos en visited (para A)
    for destino in dic_entrada[num_ml]:
        if destino <= L:  # mailing list
            if destino not in visited_ml:
                visited_ml.add(destino)
                marcar_unicos(destino)
        else:  # mail directo
            visited_mails.add(destino)


# Input
N, L = map(int, input().split())
dic_entrada = {}

for i in range(1, L + 1):
    datos = list(map(int, input().split()))
    dic_entrada[i] = datos[1:]

memo_total = {}
visited_ml = set()
visited_mails = set()

# Calcular B (con duplicados)
B = contar_total(1) % MOD

# Calcular A (sin duplicados)
visited_ml.add(1)
marcar_unicos(1)
A = len(visited_mails) % MOD

print(B, A)
