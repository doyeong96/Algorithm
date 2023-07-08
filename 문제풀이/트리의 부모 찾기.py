# https://www.acmicpc.net/problem/18870
import sys

sys.stdin = open("sample.txt", 'r')
''' 
그래프 연결
탐색 타고 처음 나오는 노드가 부모
'''

from collections import deque


def bfs(now):
    Q = deque()
    Q.append(now)
    while Q:
        x = Q.popleft()
        for nx in G[x]:
            if vis[nx] == 0:
                vis[nx] = x
                Q.append(nx)


n = int(input())
vis = [0] * (n + 1)
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

bfs(1)

for i in range(2, n + 1):
    print(vis[i])
