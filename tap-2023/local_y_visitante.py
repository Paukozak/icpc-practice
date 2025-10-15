A1, P1 = map(int, input().split())
A2, P2 = map(int, input().split())


if (A1+A2) > (P1+P2):
    print("A")
elif (A1+A2) < (P1+P2):
    print("P")
else:
    print("D")