import sys

stuff_num,max_weight=list(map(int,sys.stdin.readline().strip().split()))

weight_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(stuff_num)]


dp=[0]*(max_weight+1)
dp[0]=0
for weight,cost in weight_list: # 무게 내림차순, 가치 내림차순으로 되어있음
    for i in range(max_weight,weight-1,-1): # 무게를 많이 담는 것부터 해야함
        dp[i]=max(dp[i],dp[i-weight]+cost)

print(dp[max_weight])

# 무게가 가벼운것부터 담는건 무한정 담을 수 있을 때 하는 것