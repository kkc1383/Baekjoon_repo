import sys

n,m,b=list(map(int, sys.stdin.readline().rstrip().split()))
land_map=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)] # 2차원 배열 뚝딱

min_height=min(map(min,land_map))
max_height=max(map(max,land_map))

min_time=float('inf')
result_height=0
for height in range(min_height,max_height+1): # 최소 높이 부터 최대 높이까지 다 해보는 것
    sum_time=0
    sum_gap=0
    for i in range(n):
        for j in range(m):
            gap=land_map[i][j]-height
            sum_gap+=gap
            if gap>=0:
                sum_time+=(gap*2)
            else :
                sum_time+=abs(gap)
    
    if sum_gap+b>=0 and sum_time<=min_time :
        min_time=sum_time
        result_height=height

print(f'{min_time} {result_height}')

# python3에선 안되고 pypy3에서만 됨 (시간 초과)'
# 이 문제는 brute force문제이고 기준으로 설정할 땅의 높이가 그것이다.
# 처음에는 기준으로 설정할 땅의 높이를 평균,평균+1만 생각했었는데 깎기만하면 되는 부분에 대해선 생각하지 못했다.