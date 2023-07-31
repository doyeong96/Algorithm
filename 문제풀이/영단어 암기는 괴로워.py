import sys

sys.stdin = open('sample', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for _ in range(n):
    w = input().strip()
    if len(w) >= m:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
# print(d)
sd = sorted(d.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
# print(sd)

for a in sd:
    print(a[0])