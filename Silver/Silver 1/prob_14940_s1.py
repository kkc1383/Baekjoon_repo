from collections import deque
import sys

y_num,x_num=list(map(int,sys.stdin.readline().strip().split()))


INF=float('inf')
start_point=None
# dist=[[INF]*x_num for _ in range(y_num)]
land_map=[]
for y in range(y_num):
    line=list(map(int,sys.stdin.readline().strip().split()))
    for x in range(x_num):
        # if line[x]!=0:
        #     dist[y][x]=1
        if line[x]==2:
            start_point=(y,x)
    land_map.append(line)
# for i in range(max(y_num,x_num)):
#     dist[i][i]=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

myqueue=deque([start_point])

dist=[[0]*(x_num) for _ in range(y_num)]
while myqueue:
    top_y,top_x=myqueue.popleft()
    # if visited[top_y][top_x]: # 이거는 전체 순회를 해야할때나 하는거고
    #     continue
    for k in range(4):
        new_y=top_y+dy[k]
        new_x=top_x+dx[k]
        if new_y>=y_num or new_y<0 or new_x>=x_num or new_x<0: # 범위를 벗어났거나
            continue
        if land_map[new_y][new_x]==1: # 방문을 안했고 벽이 아닐 경우
            myqueue.append((new_y,new_x))
            dist[new_y][new_x]=dist[top_y][top_x]+1
            land_map[new_y][new_x]=2

for y in range(y_num):
    for x in range(x_num):
        if land_map[y][x]==1:
            dist[y][x]=-1

for i in range(y_num):
    print(*dist[i], sep=' ')

# 문제를 잘 읽자 원래 땅인데 갈수 없는 곳은 -1을 출력해야 한다.
# 여기서는 방문 여부를 맵을 2로 변경시켜서 확인하였다. 출발지점이 2로 표기된것을 활용했음
# 그래서 bfs를 돌고 난 후에도 아직 1이라는 것은 도달하지 못하는 땅이므로 그 좌표만 dist에 -1로 넣었음