# https://www.acmicpc.net/problem/1240
import sys

sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
풀이 방법
1. 양방향 그래프 생성 (연결 노드, 이동 비용)
2. 시작 노드를 기준으로 dfs 탐방 시작
3. 첫 시작 위치를 방문 처리(중요)
4. 현재 위치가 종료 위치와 동일 하면 이동거리를 저장
'''


def dfs(now, end, cost):
    global C
    if now == end:
        C += cost
        return
    for nxt, co in g[now]:
        if vis[nxt] == 0:
            vis[nxt] = 1
            dfs(nxt, end, cost + co)


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, cos = map(int, input().split())
    g[a].append((b, cos))
    g[b].append((a, cos))

for _ in range(m):
    s, e = map(int, input().split())
    vis = [0] * (n + 1)
    vis[s] = 1
    C = 0
    dfs(s, e, 0)
    print(C)
