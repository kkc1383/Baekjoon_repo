import sys

n=int(sys.stdin.readline().strip())

dp=[0]*12
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(n):
    input_value=int(sys.stdin.readline().rstrip())
    print(dp[input_value])


# 진짜 진짜 개빡친다 이걸 어떻게 생각하지
# 해당 수를 1,2,3으로 표기하려면 n-1을 1,2,3으로 표기한거에 마지막에 +1한거임 순서 상관있어서 맨뒤에 따른거 올수 있는거 아니냐?
# 맞다. 그래서 n-2를 1,2,3 표기한거 마지막에 +2한거랑, n-3를 1,2,3표기한거 마지막에 +3 한거
# 원초적으로 마지막 자리에 1,2,3 밖에 못오기 때문에 그 경우의 수만 착안해서 점화식을 만든거임 개미친 천재들
# 따라서 점화식은 dp[i]=dp[i-1]+dp[i-2]+dp[i-3] 이다. 초기값을 3까지 잡아놓고 4부터 돌리면 됨