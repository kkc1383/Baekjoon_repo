import sys

n=int(sys.stdin.readline().rstrip())

dp=[0]*101 # dp[index]=변의 길이
dp[0]=0
dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2
dp[6]=3
dp[7]=4
dp[8]=5

for _ in range(n):
    problem=int(sys.stdin.readline().rstrip())
    if problem>=9:
        for i in range(9,problem+1):
            dp[i]=dp[i-5]+dp[i-1]
    print(dp[problem])