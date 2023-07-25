import sys

sys.stdin = open('sample', 'r')

from collections import deque

a = deque(input())
b = deque(input())
c = False  # 안되는게 기준
while len(a) <= len(b):
    if a != b:
        if b[-1] == 'A':
            b.pop()
        else:
            b.pop()
            b.reverse()
    else:
        c = True
        break

if c:
    print(1)
else:
    print(0)