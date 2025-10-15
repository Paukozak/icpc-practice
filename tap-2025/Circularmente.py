import sys


def fft(a, invert):
	n = len(a)
	j = 0
	for i in range(1, n):
		bit = n >> 1
		while j & bit:
			j ^= bit
			bit >>= 1
		j ^= bit
		if i < j:
			a[i], a[j] = a[j], a[i]
	length = 2
	import math
	while length <= n:
		ang = 2 * math.pi / length * (-1 if invert else 1)
		wlen = complex(math.cos(ang), math.sin(ang))
		i = 0
		while i < n:
			w = 1+0j
			for j in range(i, i + length // 2):
				u = a[j]
				v = a[j + length // 2] * w
				a[j] = u + v
				a[j + length // 2] = u - v
				w *= wlen
			i += length
		length <<= 1
	if invert:
		for i in range(n):
			a[i] /= n


def convolution(a, b):
	# a, b are lists of numbers (0/1). Return linear convolution list
	n = 1
	tot = len(a) + len(b) - 1
	while n < tot:
		n <<= 1
	fa = [complex(x, 0) for x in a] + [0j] * (n - len(a))
	fb = [complex(x, 0) for x in b] + [0j] * (n - len(b))
	fft(fa, False)
	fft(fb, False)
	for i in range(n):
		fa[i] *= fb[i]
	fft(fa, True)
	res = [0] * tot
	for i in range(tot):
		res[i] = int(fa[i].real + 0.5)
	return res


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(data)
	n = int(next(it))
	p = [int(next(it)) - 1 for _ in range(n)]
	pos = [0] * n
	for i, val in enumerate(p):
		pos[val] = i

	S = [0] * n
	T = [0] * n
	for j in range(n):
		S[j] = (j + p[j]) % n
	for b in range(n):
		T[b] = (b + pos[b]) % n

	groupsJ = {}
	groupsB = {}
	for j, r in enumerate(S):
		groupsJ.setdefault(r, []).append(j)
	for b, r in enumerate(T):
		groupsB.setdefault(r, []).append(b)

	# prepare counts of k (0..n-1)
	cnt = [0] * n

	# threshold for small groups -> brute force pairs; else FFT
	# tuned to balance; use 700 as starting point
	THRESH = 700

	for r, J in groupsJ.items():
		B = groupsB.get(r, [])
		if not B:
			continue
		szJ = len(J)
		szB = len(B)
		if szJ * szB <= THRESH * max(1, szJ + szB):
			# direct
			for j in J:
				for b in B:
					k = j - b
					k %= n
					cnt[k] += 1
		else:
			# use convolution: A[j]=1 if j in J; B_rev[idx]=1 where idx=n-1-b
			A = [0] * n
			Brev = [0] * n
			for j in J:
				A[j] = 1
			for b in B:
				Brev[n - 1 - b] = 1
			conv = convolution(A, Brev)  # length 2n-1
			# conv[n-1 + k] corresponds to difference k
			base = n - 1
			for k in range(n):
				val = conv[base + k]
				if val:
					cnt[k] += val

	# cnt[k] now equals number of pairs (j,b) satisfying S_j==T_b and j-b==k
	# This equals s(rot_k)
	total = sum(cnt)
	print(total)


if __name__ == '__main__':
	main()

