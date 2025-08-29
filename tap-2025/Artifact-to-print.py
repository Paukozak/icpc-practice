palabra=input()
i=0
formo=False

while i < len(palabra):
    if palabra[i] == "T":
        i += 1
        while i < len(palabra):
            if palabra[i] == "A":
                i += 1
                while i < len(palabra):
                    if palabra[i] == "P":
                        formo = True
                        break   
                    i += 1
                break  
            i += 1
        break  
    i += 1

if formo:
    print("S")
else:
    print("N")