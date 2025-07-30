import sys

city_num=int(sys.stdin.readline().strip())
edge_num=int(sys.stdin.readline().strip())

dist=[[float('inf')]*(city_num) for _ in range(city_num)]


for _ in range(edge_num):
    start,end,cost=list(map(int,sys.stdin.readline().strip().split()))
    dist[start-1][end-1]=min(dist[start-1][end-1],cost) # 중복 간선이 있기 때문에 최솟값만 남기면 됨. 이 문제의 핵심


for i in range(city_num):
    dist[i][i]=0

for k in range(city_num):
    for i in range(city_num):
        for j in range(city_num):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

for i in range(city_num):
    for j in range(city_num):
        if dist[i][j]==float("inf"):
            dist[i][j]=0

for line in dist:
    print(*line,sep=" ")

# 못가는 쪽으로는 0을 출력하는 것도 해야하는데