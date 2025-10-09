import random
import subprocess
import sys

# run a few random tests for small X
PY = sys.executable
for X in range(1,2000):
    # generate full divisors of X
    divs = [d for d in range(1, X+1) if X % d == 0]
    m = len(divs)
    if m <= 1:
        continue
    # choose one missing
    miss = random.randrange(m)
    arr = divs[:miss] + divs[miss+1:]
    # shuffle
    random.shuffle(arr)
    inp = str(m-1) + '\n' + ' '.join(map(str, arr)) + '\n'
    p = subprocess.Popen([PY, 'd:/icpc-practice/tap-2025/Hidden-divisor.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out,err = p.communicate(inp)
    out = out.strip()
    if out == '*':
        # solver says ambiguous/wrong; check if actually ambiguous
        # brute force: check all Y 1..1e6 consistent
        sols = []
        for Y in range(1,5000):
            dvs = [d for d in range(1, Y+1) if Y % d == 0]
            if len(dvs) != m:
                continue
            if set(arr) == set(dvs) - set([next(iter(set(dvs)-set(arr)))]):
                pass
        # skip deep check for now; only report if solver output is inconsistent with expected unique solution
        # we'll just print examples where solver returned * but actual unique exists
        # to detect unique, brute-force check all Y up to, say, 2000
        sols = []
        for Y in range(1,2000):
            dvs = [d for d in range(1, Y+1) if Y % d == 0]
            if len(dvs) != m:
                continue
            if set(arr) == set(dvs) - set([d for d in dvs if d not in arr][0:1]):
                sols.append(Y)
        if len(sols) == 1:
            print('Found bad: X=', X, 'missing=', divs[miss], 'solver=* but unique Y=', sols[0])
            print('input:', inp)
            break
    else:
        # solver printed 'L miss'
        try:
            L,missout = map(int, out.split())
        except:
            print('bad parse', out)
            break
        # check correctness
        if L != X or missout != divs[miss]:
            print('Found mismatch: X=', X, 'expected', X, divs[miss], 'got', out)
            print('input:', inp)
            break
print('done')
