import sys

sys.stdin = open('sample', 'r')

from collections import deque

def dfs(tar):
    global c
    if s == tar:
        c = 1
        return

    if len(tar) == 0:
        return

    if tar[-1] == 'A':
        dfs(tar[:-1])

    if tar[0] == 'B':
        dfs(tar[1:][::-1])

s = input()
t = input() # 만들어야 하는 문자
c = 0

dfs(t)
print(c)



