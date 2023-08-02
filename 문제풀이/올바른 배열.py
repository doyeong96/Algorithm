import sys

sys.stdin = open('sample', 'r')
input = sys.stdin.readline

INF = 987654321
n = int(input())
li = [int(input()) for _ in range(n)]
minV = INF

for num in li:
    cnt = 0
    for i in range(num,num+5):
        if i not in li:
            cnt +=1
    if minV > cnt:
        minV = cnt

print(minV)

