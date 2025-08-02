import sys

house_num=int(sys.stdin.readline().strip())

color_cost_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(house_num)]   # color_cost_list[k][0]은 빨강, 1은 초록 2는 파랑


dp=[[float('inf')]*3 for _ in range(house_num)]
dp[0][0]=color_cost_list[0][0]
dp[0][1]=color_cost_list[0][1]
dp[0][2]=color_cost_list[0][2]


for house in range(1,house_num):
    for color in range(3): # 0은 빨강, 1은 초록, 2는 파랑
        dp[house][color]=min(dp[house][color], # 기존게 좋거나
                             dp[house-1][(color+1)%3]+color_cost_list[house][color], # 이전 집에서 지금과 다른 색을 칠한경우
                             dp[house-1][(color+2)%3]+color_cost_list[house][color]  # 이전의 집에서 또 다른 색을 칠한경우
                             )

print(min(dp[house_num-1][0],dp[house_num-1][1],dp[house_num-1][2]))