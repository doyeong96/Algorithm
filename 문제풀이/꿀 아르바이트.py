# https://www.acmicpc.net/problem/12847
import sys

sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
접근방법 = 구간합 + 슬라이딩 윈도우

구간합 배열을 만들어두고
일할수 있는 범위를 윈도우 범위로 만들어둔다
=> 시작일 = 1, 종료일 = m (구간합 배열을 이용해 계산하기 때문에 시작일을 1일으로 해둔다)
구간합 배열에서 계산한다 ps[e] - ps[s-1]
최대값을 찾는다
'''
INF = 987654321
n, m = map(int, input().split())
li = list(map(int, input().split()))
ps = [0] * (n + 1)

for i in range(1, n + 1):
    ps[i] = ps[i - 1] + li[i - 1]
maxV = -INF

# print(ps)
s, e = 1, m
while e < n + 1:
    a = ps[e]
    b = ps[s-1]
    # a = ps[e] - ps[s - 1]
    # print(a-b)
    maxV = max(maxV, ps[e] - ps[s - 1])
    s += 1
    e += 1
print(maxV)
