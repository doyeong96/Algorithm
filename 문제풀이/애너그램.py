import sys

sys.stdin = open('sample', 'r')
input = sys.stdin.readline


def bt(now, ans):
    if now == m:
        print(ans)

    for i in range(m):
        if vis[i] == 0:
            tmp = ans + w[i]
            if tmp not in used:
                # ans += w[i]
                used.add(ans)
                vis[i] = 1
                bt(now + 1, ans + w[i])
                vis[i] = 0


n = int(input())
for _ in range(n):
    w = sorted(list(input().strip()))
    m = len(w)
    vis = [0] * m
    used = set()

    bt(0, "")
