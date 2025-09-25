import sys
import random

# Usage: python bench_gen.py N G maxT out_path
if len(sys.argv) < 5:
    print("Usage: bench_gen.py N G maxT out_path")
    sys.exit(1)

N = int(sys.argv[1])
G = int(sys.argv[2])
maxT = int(sys.argv[3])
out_path = sys.argv[4]

random.seed(0)
with open(out_path, 'w') as f:
    f.write(f"{N} {G}\n")
    arr = [str(random.randint(1, maxT)) for _ in range(N)]
    f.write(' '.join(arr) + '\n')
