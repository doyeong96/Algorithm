# https://www.acmicpc.net/problem/1935
import sys

sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
풀이 아이디어
1. 연산자와 피 연산자를 구분해야한다
=> 연산자를 배열로 선언해주고 미리 할당(어차피 변화하지 않는다)
2. 반복문을 돌며 피 연산자라면 해당하는 숫자를 num 배열에 저장
=> 아스키코드를 이용해서 nums 배열의 인덱스위치를 찾아갈 수 있게 한다
3. 연산자를 만나면 num 배열에서 두개의 숫자를 빼온다.
=> 후위표기식이기 때문에 두번째 숫자가 더 뒤에 있어야한다.
4. f-string 을 이용해서 소수점 아래 값을 출력
'''

n = int(input())
li = list(input().strip())
nums = [int(input()) for _ in range(n)]

num = []
# print(ord('A')-64)
calc = ['*', '/', '+', '-']
for j in range(len(li)):
    if li[j] not in calc:
        num.append(nums[ord(li[j]) - 65])
    else:
        a = num.pop()
        b = num.pop()

        if li[j] == calc[0]:
            b *= a
        elif li[j] == calc[1]:
            b /= a
        elif li[j] == calc[2]:
            b += a
        else:
            b -= a
        num.append(b)
print(f'{num[-1]:.2f}')
