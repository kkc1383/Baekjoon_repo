import sys

num,ans_num=list(map(int,sys.stdin.readline().strip().split()))

num_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(num)]
ans_xy_list=[]
for _ in range(ans_num):
    start_y,start_x,end_y,end_x=list(map(int,sys.stdin.readline().strip().split()))
    ans_xy_list.append([(start_y-1,start_x-1),(end_y-1,end_x-1)])

dp=[[0]*num for _ in range(num)]

dp[0][0]=num_list[0][0]

for n in range(1,num): # 첫 행과 첫 열만 채우기
    dp[0][n]=dp[0][n-1]+num_list[0][n]
    dp[n][0]=dp[n-1][0]+num_list[n][0]

for y in range(1,num): # 그 외 dp 테이블 채우기
    for x in range(1,num):
        dp[y][x]=dp[y-1][x]+dp[y][x-1]-dp[y-1][x-1]+num_list[y][x]

for [(s_y,s_x),(e_y,e_x)] in ans_xy_list:
    if s_y==0 and s_x==0: # 시작지점이 (0,0)일 때
        print(dp[e_y][e_x])
    elif s_y==0: # 시작지점이 (x,0)일 때
        print(dp[e_y][e_x]-dp[e_y][s_x-1])
    elif s_x==0: # 시작지점이 (0,y)일 때
        print(dp[e_y][e_x]-dp[s_y-1][e_x])
    else: # 시작지점이 (x,y) 일 때
        print(dp[e_y][e_x]-(dp[e_y][s_x-1]+dp[s_y-1][e_x]-dp[s_y-1][s_x-1]))
    
    
# dp는 x,y까지의 전체 합
# dp[y][x]=dp[y-1][x]+dp[y][x-1]-dp[y-1][x-1]+num_list[y][x] 이 공식 이해하는게 중요