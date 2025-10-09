class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        posiciones = []
        letras = []
        for x in range(len(s)):
            if s[x] in vowels:
                posiciones.append(x)
                letras.append(s[x])
        vocalesordenadas = sorted(letras)
        i = 0
        for x in posiciones:
            s = s[:x] + vocalesordenadas[i] + s[x+1:]
            i+=1
        return s