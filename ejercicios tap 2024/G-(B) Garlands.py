S = input()
gaylands = 0
bandera = True
while bandera:
    if 'T' in S:
        if 'P' in S:
            if ('U' in S): 
                gaylands+= 1
                S = S.replace('T', '', 1)
                S = S.replace('P', '', 1)
                S = S.replace('U', '', 1)
            elif ('A' in S):
                gaylands+= 1
                S = S.replace('T', '', 1)
                S = S.replace('P', '', 1)
                S = S.replace('A', '', 1)
            else:
                bandera = False
        else:
            bandera = False
    else:
        bandera = False

print(gaylands)