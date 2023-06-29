# https://www.acmicpc.net/problem/1240
import sys

sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
풀이 방법
1. 양방향 그래프 생성 (연결 노드, 이동 비용)
2. 시작 노드를 기준으로 bfs 탐방 시작
3. 탐방을 하며 현재 위치가 종료 지점과 동일하면 종료
'''

from collections import deque


def bfs(s, e):
    Q = deque()
    Q.append((s, 0))
    vis[s] = 1
    while Q:
        now, co = Q.popleft()
        if now == e:
            return co
        for nxt, cos in g[now]:
            if vis[nxt] == 0:
                vis[nxt] = 1
                Q.append((nxt, co + cos))


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, cos = map(int, input().split())
    g[a].append((b, cos))
    g[b].append((a, cos))


for _ in range(m):
    s, e = map(int, input().split())
    vis = [0] * (n + 1)
    print(bfs(s, e))
