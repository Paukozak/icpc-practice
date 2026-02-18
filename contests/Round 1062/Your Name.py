q = int(input())
for i in range(q):
    n = int(input())
    A = input()    
    palabras = A.split(' ')
    cubos = palabras[0]
    nombre = palabras[1]

    bandera = True
    for x in cubos:
        salida = nombre.find(x)
        if salida == -1:
            bandera = False
            break
        else:
            nombre = nombre[:salida] + nombre[salida + 1:]

    if bandera and len(nombre) == 0:
        print('YES')
    else:
        print('NO')
