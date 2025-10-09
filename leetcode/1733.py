class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        problemas = []
        langhablado = {}
        for amistad in friendships:
            amigo1 = amistad[0]-1 #Es -1 por los indices de python
            amigo2 = amistad[1]-1 #Es -1 por los indices de python
            lenguas1 = languages[amigo1] #Idiomas del amigo1 
            lenguas2 = languages[amigo2] #Idiomas del amigo2
            lenguajesmutuos = set(lenguas1) & set(lenguas2) #Interseccion de idiomas
            if list(lenguajesmutuos) == []: #Si no hablan ningun lenguaje mutuamente
                if amigo1 not in problemas: #Si no almacene al amigo1
                    problemas.append(amigo1+1) #Guardo al amigo
                    for lenguajes in list(lenguas1): #Cuento sus idiomas
                        langhablado[lenguajes] = langhablado.get(lenguajes, 0) + 1
                if amigo2 not in problemas: #Si no almacene al amigo2
                    problemas.append(amigo2+1) #Guardo al amigo
                    for lenguajes in list(lenguas2): #Cuento sus idiomas
                        langhablado[lenguajes] = langhablado.get(lenguajes, 0) + 1
        lenguajemashablado = max(langhablado.values(), default=0)
        return (len(problemas)-lenguajemashablado)