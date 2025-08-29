A, B, C = map(int, input().split())

cambio = B - A
if cambio % C == 0:
    print("S")
else:
    print("N")