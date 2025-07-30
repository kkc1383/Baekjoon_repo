from collections import defaultdict
import sys


n=int(sys.stdin.readline().strip())

dist=[[0]*n for _ in range(n)]

for y in range(n):
    line=list(map(int,sys.stdin.readline().strip().split()))
    for x in range(n):
        if line[x]==1:
            dist[y][x]=1

# for i in range(n): # 최단 거리 구할때는 dist[i][i]=0의 초기화가 필요함 근데 지금은 길의 유무를 판단하기 때문에 오판을 방지하기 위해 본인은 건드리지 않는 것이 좋음
#     dist[i][i]=1

for k in range(n):
    for y in range(n):
        for x in range(n):
            if not dist[y][x]:
                dist[y][x]=(dist[y][k] and dist[k][x])

for y in range(n):
    print(*dist[y], sep=" ")


# 자기자신을 1로 두게되면 아예 길이 없어도 길이 있는거라고 판단함.