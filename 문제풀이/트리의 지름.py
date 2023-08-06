import sys

sys.stdin = open('sample', 'r')
input = sys.stdin.readline

from collections import deque


def bfs(now, dis):
    global maxV
    vis = [0] * (n + 1)
    Q = deque()
    Q.append((now, dis))  # 현재 위치, 길이
    vis[now] = 1

    while Q:
        node, ans = Q.popleft()
        for nx, nd in g[node]:
            if vis[nx] == 0:  # 미방문 상태
                Q.append((nx, ans + nd))
                res.append((nx, ans + nd))
                vis[nx] = 1
    # l.append(dis)
    # maxV = max(maxV, dis)


INF = 987654321
n = int(input())
g = [[] for _ in range(n + 1)]  # 연걸된 노드, 가중치
maxV = -INF
for _ in range(n):
    li = list(map(int, input().split()))
    m = len(li)
    now = li[0]
    for i in range(1, m):  # 홀수 = 정점, 짝수 = 가중치
        if li[i] == -1:
            break

        if i % 2 == 1:  # 정점
            nxt = li[i]
        else:
            g[now].append((nxt, li[i]))
            # g[nxt].append((now, li[i]))
res = []
bfs(1, 0)
# print(res)
find = sorted(res, key=lambda x: -x[1])
# print(find[0][0])
res = []
bfs(find[0][0], 0)
find = sorted(res, key=lambda x: -x[1])
print(find[0][1])
# l=[]
# for i in range(1, n + 1):
#     bfs(i)
# print(l)
# print(maxV)
