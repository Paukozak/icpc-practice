A, B, C = map(int, input().split())

if ((A+B) <= C):
    print("S")
elif ((A+C) <= B):
    print("S")
elif ((B+C) <= A):
    print("S")
else:
    print("N") 


