import sys

sys.stdin = open('sample', 'r')

n = int(input())
li = input()
r = li[::-1]
ans = 'NO'
for i in range(1, n):
    a = li[:i]
    b = r[:i][::-1]
    c = 0

    for j in range(len(a)):
        if a[j] != b[j]:
            c += 1

    if c == 1:
        ans = 'YES'
        break

print(ans)
