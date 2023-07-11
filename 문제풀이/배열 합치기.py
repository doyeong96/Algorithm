import sys

sys.stdin = open("sample.txt", 'r')

n, m = map(int, input().split())
dap = []
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

s1, s2, e1, e2 = 0, 0, n, m

while s1 < e1:
    dap.append(li1[s1])
    s1 += 1

while s2 < e2:
    dap.append(li2[s2])
    s2 += 1
dap.sort()
print(*dap)