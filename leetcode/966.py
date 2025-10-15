class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        salida = []

        def mask(word: str) -> str:
            v = set("aeiou")
            return ''.join('/' if c in v else c for c in word.lower())

        palabrassinvocales = [mask(w) for w in wordlist]

        for x in queries:
            if x in wordlist:
                salida.append(x)
                continue

            qlower = x.lower()
            qmask = mask(x)

            found = False
            for idx, h in enumerate(wordlist):
                if h.lower() == qlower:
                    salida.append(h)
                    found = True
                    break
            if found:
                continue

            for idx, h in enumerate(wordlist):
                if palabrassinvocales[idx] == qmask:
                    salida.append(h)
                    found = True
                    break

            if not found:
                salida.append("")

        return salida