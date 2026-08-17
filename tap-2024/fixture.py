N = int(input())
R = input()
racha = 0
i = 0
pts = 0

while i < len(R):
    if R[i] == "1":
        pts+=1
        racha+=1
        if racha == 3:
            racha-=1
            pts+=1
    elif R[i] == "0":
        pts-=1
        racha= 0
    i+=1

print(pts)