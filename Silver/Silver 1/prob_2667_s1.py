from collections import deque
import sys

n=int(sys.stdin.readline().strip())

house_list=[] # 집의 좌표들
map_house=[] # 전체 맵
for y in range(n):
    line=list(map(int,sys.stdin.readline().strip()))
    for x in range(n):
        if line[x]==1:
            house_list.append((y,x))
    map_house.append(line)

visited=[[False]*(n) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

house_count_list=[] # 집 단지가 하나의 원소이고 그 단지별 집 갯수가 그 value
for start in house_list:
    if visited[start[0]][start[1]]:
        continue
    house_count=1
    myqueue=deque([start])
    visited[start[0]][start[1]]=True

    while myqueue:
        top_y,top_x=myqueue.popleft()
        for k in range(4):
            new_y=top_y+dy[k]
            new_x=top_x+dx[k]
            if new_y>=n or new_y<0 or new_x>=n or new_x<0:
                continue
            if not visited[new_y][new_x] and map_house[new_y][new_x]==1:
                visited[new_y][new_x]=True
                myqueue.append((new_y,new_x))
                house_count+=1
    house_count_list.append(house_count)

house_count_list.sort()
print(len(house_count_list))
for elem in house_count_list:
    print(elem)