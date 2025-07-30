from collections import deque
import sys

n=int(sys.stdin.readline().strip()) 
grid_map=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

dp=[[[0]*3 for _ in range(n)] for _ in range(n)] # 마지막 3칸은 0이 가로, 1이 세로, 2가 대각선
dp[0][1][0]=1

for i in range(n):
    for j in range(n):
        if grid_map[i][j]:
            continue
        
        # 가로일 때
        if j-1>=0 and not grid_map[i][j-1]: 
            dp[i][j][0]+=dp[i][j-1][0]+dp[i][j-1][2]
        
        #세로일 때
        if i-1>=0 and not grid_map[i-1][j]: 
            dp[i][j][1]+=dp[i-1][j][1]+dp[i-1][j][2]

        #대각선 일 때
        if i-1>=0 and j-1>=0 and not (grid_map[i][j-1] or grid_map[i-1][j] or grid_map[i-1][j-1]): 
            dp[i][j][2]+=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))


# dp로 풀면 성공
# 알기 어려웠던 것은 방향 별로 갈 수 있는 가짓수가 고정되어있었음, 예를들어 가로다음 바로 세로를 못쓴다거나
# 그리고 dp를 더할때 여러가지 버전들이 있는데 그것을 다 따로두어서 더하는 방향으로 했음
# 대각선은 세로모드일때 x-1,y-1 와 가로모드일때, 대각모드일 때 모두 더해주어야함