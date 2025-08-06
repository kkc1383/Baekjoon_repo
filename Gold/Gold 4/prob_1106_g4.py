import sys

target,city_num=list(map(int,sys.stdin.readline().strip().split())) 

info_list=[tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(city_num)] # (cost, 얻을 수 있는 고객)

dp=[float('inf')]*1101
dp[0]=0
for (cost,cust) in info_list:
    for i in range(cust,1101): # dp의 인덱스는 고객수 결과값은 비용
        dp[i]=min(dp[i],dp[i-cust]+cost)

print(min(dp[target:]))

# 이 문제는 그리디 처럼 보이지만 dp로 푸는게 맞음
# 반례가 존재 할 수 있기 때문에
# 어떻게 푸냐면 unbound knapsack처럼 푸는것이고 일단 target을 초과 되더라도 효율이 좋은 상품이 있으면 더 쌀 수도 있는 것이기 때문
# 그래서 일단 쫙 구해놓고 target이상인 dp의 최소를 가져오면 되는 것