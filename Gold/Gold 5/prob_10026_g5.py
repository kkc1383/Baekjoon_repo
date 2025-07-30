from collections import deque
import sys

n=int(sys.stdin.readline().strip())

green_list=[]
grid_map=[]
for y in range(n):
    line=list(sys.stdin.readline().strip())
    for x in range(n):
        if line[x]=="G":
            green_list.append((y,x))
    grid_map.append(line)


grid_map_weak=[row[:] for row in grid_map] # 전체 얕은 복사

for coord in green_list:
    grid_map_weak[coord[0]][coord[1]]="R"

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited_normal=[[False]*n for _ in range(n)]
visited_weak=[[False]*n for _ in range(n)]

count_normal=0
count_weak=0
for y in range(n):
    for x in range(n):
        if visited_normal[y][x]:
            continue
        count_normal+=1 # 덩어리 더하고
        myqueue=deque()
        myqueue.append((y,x)) # queue만들어 주고
        color=grid_map[y][x] # 기준이 되는 거
        visited_normal[y][x]=True # 방문 체크하고

        while myqueue:
            top_y,top_x=myqueue.popleft()
            for k in range(4):
                new_x=top_x+dx[k]
                new_y=top_y+dy[k]
                if new_x>=n or new_x<0 or new_y>=n or new_y<0:
                    continue
                if not visited_normal[new_y][new_x] and grid_map[new_y][new_x]==color:
                    myqueue.append((new_y,new_x))
                    visited_normal[new_y][new_x]=True

for y in range(n):
    for x in range(n):
        if visited_weak[y][x]:
            continue
        count_weak+=1 # 덩어리 더하고
        myqueue=deque()
        myqueue.append((y,x)) # queue만들어 주고
        color=grid_map_weak[y][x] # 기준이 되는 거
        visited_weak[y][x]=True # 방문 체크하고

        while myqueue:
            top_y,top_x=myqueue.popleft()
            for k in range(4):
                new_x=top_x+dx[k]
                new_y=top_y+dy[k]
                if new_x>=n or new_x<0 or new_y>=n or new_y<0:
                    continue
                if not visited_weak[new_y][new_x] and grid_map_weak[new_y][new_x]==color:
                    myqueue.append((new_y,new_x))
                    visited_weak[new_y][new_x]=True

print(count_normal, count_weak)
    
# 그냥 각각 상황 나눠서 두번 돌려줬음 BFS라 속도가 빠르긴 한가 봅니다.