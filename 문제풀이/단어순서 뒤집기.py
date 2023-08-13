import sys

sys.stdin = open('sample', 'r')
input = sys.stdin.readline

from collections import deque

n = int(input())
for i in range(1,n+1):
    st = []
    w = input().split()
    for a in w:
        st.append(a)
    print(f'Case #{i}:', end =" ")
    while st:
        print(st.pop(), end=" ")
    print()
    # for s in st:
    #     print(s, end="")