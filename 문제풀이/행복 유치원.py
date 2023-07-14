import sys

sys.stdin = open("sample.txt", 'r')
'''
m개의 조를 만든다고 해서 그 조에 같은 인원이 배분될 필요는 없다!
[0],[1,2,3],[4] 로 조를 만들더라도 3개의 조를 만든것
'''
n, m = map(int, input().split())
li = list(map(int, input().split()))
ps = [0] * (n-1)

for i in range(n - 1):
    ps[i] = li[i + 1] - li[i]
ps.sort()
# print(ps)

cnt = 0

for i in range(n - m):
    # print(i)
    cnt += ps[i]
print(cnt)
