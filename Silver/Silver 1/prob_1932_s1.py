import sys

n=int(sys.stdin.readline().strip())

num_list=[]
for i in range(n):
    input_value=list(map(int,sys.stdin.readline().strip().split()))
    input_value+=[0]*(n-i-1)
    num_list.append(input_value)

dp=[[0]*n for _ in range(n)]

dp[0][0]=num_list[0][0]

if n==1:
    print(dp[0][0])
else:
    for y in range(n):
        for x in range(n):
            dp[y][x]=max(dp[y][x], dp[y-1][x]+num_list[y][x], dp[y-1][x-1]+num_list[y][x])

    print(max(dp[n-1]))