N = int(input())
tablero = []
cant = 0

for x in range(N):
    bandera = False
    A = input()
    for y in A:
        if y == 'N':
            if bandera:
                cant+= 1
                bandera = False
            else:    
                bandera = True
        else:
            bandera = False
            
print(cant)