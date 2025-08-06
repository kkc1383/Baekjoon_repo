import sys

coin_num, target=list(map(int,sys.stdin.readline().strip().split()))

coin_list=[int(sys.stdin.readline().strip()) for _ in range(coin_num)]  

dp=[0]*(target+1)
dp[0]=1

for coin in coin_list:
    for i in range(coin,target+1):
        dp[i]+=dp[i-coin]

print(dp[target])