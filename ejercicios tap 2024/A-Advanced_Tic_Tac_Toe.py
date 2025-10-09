N = int(input())
blockers = [[] for _ in range(9)]  # blockers[i]: lista de celdas que deben estar ocupadas para poder usar i

for _ in range(N):
    A, B = map(int, input().split())
    blockers[B-1].append(A-1)

# Chequea si hay ganador usando bitmask
def check_winner(xmask, omask):
    wins = [
        0b111000000, 0b000111000, 0b000000111, # filas
        0b100100100, 0b010010010, 0b001001001, # columnas
        0b100010001, 0b001010100              # diagonales
    ]
    for w in wins:
        if (xmask & w) == w:
            return 1
        if (omask & w) == w:
            return 2
    return 0

# Devuelve lista de celdas disponibles según restricciones y tablero
def get_available(xmask, omask):
    available = []
    for i in range(9):
        if ((xmask | omask) >> i) & 1:
            continue
        blocked = False
        for a in blockers[i]:
            if ((xmask | omask) >> a) & 1 == 0:
                blocked = True
                break
        if not blocked:
            available.append(i)
    return available

memo = {}

def minimax(xmask, omask, turn):
    key = (xmask, omask, turn)
    if key in memo:
        return memo[key]

    winner = check_winner(xmask, omask)
    if winner == 1:
        memo[key] = 1
        return 1
    if winner == 2:
        memo[key] = -1
        return -1
    if (xmask | omask) == 0b111111111 or not get_available(xmask, omask):
        memo[key] = 0
        return 0

    moves = get_available(xmask, omask)
    if turn == 1:
        value = -2
        for move in moves:
            value = max(value, minimax(xmask | (1 << move), omask, 2))
            if value == 1:
                break
        memo[key] = value
        return value
    else:
        value = 2
        for move in moves:
            value = min(value, minimax(xmask, omask | (1 << move), 1))
            if value == -1:
                break
        memo[key] = value
        return value

result = minimax(0, 0, 1)
if result == 1:
    print("X")
elif result == -1:
    print("O")
else:
    print("E")