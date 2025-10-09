N=int(input())

cant=0

for i in range(N):
    casillas = input()
    
    negras=0
    
    for casilla in casillas:
        if casilla=="N":
            negras+=1
        else:
            negras=0
            
        if negras==2:
            cant+=1
            negras=0
        
        
print(cant)
