# Algorithm

> 나는 알고리즘을 못하니까 열심히 공부하자
> 
> 알고리즘 공부와 풀이한 문제를 정리하는 레포지토리 입니다.

## 1. INDEX

[백준](https://github.com/siwon-park/Problem_Solving/tree/main/Baekjoon_Solve)
[프로그래머스](https://github.com/siwon-park/Problem_Solving/tree/main/Programmers_Solve)
<br>

## 2. 코딩 테스트 공부법

류호석 선생님의 코딩 테스트 공부법 소개 中

### 1. 정확하게 이해하고 넘어가자

한 문제에 30분을 쓰고 대충 넘어가는 것보다 3 ~ 4시간을 쓰더라도 제대로 푸는 게 낫다.
완벽하게 이해하면 다음에 비슷한 문제가 나와도 훨씬 수월하게 풀 수 있고, 푸는 시간도 단축된다.

- 어떻게 하면 보다 정확하게 이해할 수 있을까?
  - **질문을 정리하다 보면 이해력과 문제 해결력이 상승한다**
    
    #### 1) 짝을 이뤄서 서로에게 설명하기(스터디)
    
    스터디를 하면서 서로에게 **문제에 대한 설명, 풀이, 접근 방법**까지 전부 다 세세하게 설명한다.
    청취자는 트집을 잡을 기세로 설명을 잘 듣고, 설명하는 사람은 듣는 사람이 잘 이해하고 있는지 체크하면서 진행
- 코드 설명까지 하려면 언어를 통일해야하지만, 사실 중요한 것은 풀이이기 때문에 풀이까지만 진행해도 됨
  
  <br>
  #### 2) 주석을 정말 완전 최고로 열심히 달기
  문장(S + V + @) 형태로 주석을 달 것.
- 변수는 의미를 쓴다.
- 조건문은 왜 썼는지, 무엇을 하기 위한 조건문인지 쓴다.
- 함수는 어떤 변수를 받아서 동작을 어떻게 하는지, 시간복잡도는 얼마인지까지 쓴다.
  - 문제를 풀었는데, 시간초과가 난다면 시간 복잡도를 봐야한다. 이 때, 함수별로 미리 시간 복잡도를 적어두면 어디서 시간초과가 나는지 쉽게 파악할 수도 있다.
    어색하면 100% 이해를 못한 것이니 주석을 읽었을 때 문장, 설명이 어색하지 않아야 한다.
    10년 뒤에 해당 코드를 보더라도 이해가 갈 정도로 자세히 주석을 달아야 한다.
    주석을 정말 잘 달면 문제가 발생한 곳을 더 빨리 캐치할 가능성이 높아진다 => 디버깅 시 이점
    
    <br>
    ### 2. 시간을 정해놓고 풀자
    다이어트를 하려면 현재 몸무게를 재야하듯이 코딩 테스트 통과를 위해서는 시간을 측정하는 것이 필요하다!
    #### 1) 시간을 정해놓고 정한 만큼 쓰자
    문제 난이도별 사용할 시간의 min, max를 정해놓자
- Silver: 30분 ~ 1시간
- Gold: 30분 ~ 2시간
- 삼성 기출: 1시간 ~ 2시간
  
  #### 2) 처음부터 다시 풀 것
  
  정해진 시간을 초과했을 때도 못 풀면 해설을 보고 완벽하게 이해하자.
  그리고 나서 코드를 싹 다 지우고 다시 처음부터 풀어보자.  즉시 풀어도 좋지만, 최소 3일 ~ 7일이 지나서 머리 속에서 완전히 날린 뒤에 푸는 것이 더 효과적이다. 단, 반드시 꼭 꼭 다시 풀 것!!
  Q) 다시 푸는 것이 과연 의미가 있는가?
  A) 100% 그렇다. 왜냐하면 해설을 본다고 해서 전부 다 이해하는 것은 아니기 때문이다. 해당 과정을 통해서
  - 막힌 부분이 해결되는지 확인
  - 실수가 줄어드는지 확인
  - 풀이 시간이 줄어드는지 확인
    할 수 있다.  (특정 알고리즘을 공부 중이라면 다른 사람의 코드를 적극 활용해도 괜찮다.)
    
    #### 3) "조금만 더하면 풀 수 있을 것 같은데"의 함정에 빠지지 말자
    
    시간이 지나면 칼 같이 끊고 해설을 본 다음, 깨끗하게 처음부터 다시 도전해보자
    
    <br>
    ### 3. 3가지 질문에 대해 답해보기
    #### 1) 시간 복잡도
    각 단계별로 시간 복잡도가 어느 정도고, 총 얼마인지 계산하는 습관을 들일 것
    #### 2) 공간 복잡도
    사용한 자료 구조의 공간 복잡도는 얼마인지 계산, 설명해보기
    #### 3) 어려웠던 부분?, 핵심은 무엇?
    문제를 풀면서 가장 어렵다고 생각했던 부분, 왜 어려웠는지?
    문재의 핵심이 되는 부분은 무엇이었는지?
    경우에 따라서 문제가 너무 쉬워서 이런 부분이 떠오르지 않을 수도 있는데, 그렇다고 하더라도 짜내서 뭐라도 쓰기
