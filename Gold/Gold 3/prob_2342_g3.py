import sys

action_list=list(map(int,sys.stdin.readline().strip().split()))
del action_list[-1]

dp=[[float("inf")]*5 for _ in range(5)]

def cost(start,end): # 0: 중앙, 1: 위쪽, 2:왼쪽, 3:아래쪽, 4:오른쪽
    if start==0:
        return 2
    elif start==end:
        return 1
    else:
        opposite={1:3,2:4,3:1,4:2}
        if opposite[start]==end: # 정 반대 일경우
            return 4
        else:
            return 3
        
dp[0][0]=0
for act in action_list:
    new_dp=[[float("inf")]*5 for _ in range(5)]
    for left in range(5):
        for right in range(5):
            new_dp[act][right]=min(new_dp[act][right],dp[left][right]+cost(left,act)) # 왼쪽발이 움직일떄
            new_dp[left][act]=min(new_dp[left][act],dp[left][right]+cost(right,act)) # 오른쪽발이 움직일때
    
    dp=new_dp

print(min(min(row) for row in dp)) # 2차원배열에서 최소값 한줄로 표기하는 방법

# 일단 최소값을 구하는것은 inf로 초기값설정하는것을 잊지말자 그리고 첫 스타트는 0 초기값 설정도
# 그리고 생각보다 dp는 브루트포스의 느낌이 강함 생각보다 모든 경우의 수를 다 계산하는 것임
# 그래서 이것도 왼쪽발 오른쪽발에 대해서 전부 게산하게 된다.
# 그리고 슬라이딩 윈도 기법을 이용해서 n*5*5를 만드는것이 아니고 5*5를 차례차례 내려가면서 사용
# 어짜피 이전 행동만 있으면 되기 때문에 새로운거 만들어놓고 바꿔가는 식으로 하는게 메모리 절약에 좋음
