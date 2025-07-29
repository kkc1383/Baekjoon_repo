from collections import deque
import sys

n=int(sys.stdin.readline().strip())
rain_map=[[0] * n for _ in range(n)]
for i in range(n):
    rain_map[i]=list(map(int,sys.stdin.readline().strip().split()))

max_num=max(map(max,rain_map))
max_area=0

DIR=[(1,0),(-1,0),(0,1),(0,-1)]
def visited_fill(i,j,level,visited):
    q=deque([(i,j)])
    visited.add((i,j))

    while q:
        x,y=q.popleft()
        for dx, dy in DIR:
            nx, ny=x+dx, y+dy
            if 0 <= nx < n and 0<= ny < n:
                if rain_map[nx][ny]> level and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny))

    
for level in range(max_num):
    area=0
    visited=set()
    for i in range(n):
        for j in range(n):
            if rain_map[i][j]>level:
                if not (i,j) in visited :
                    area+=1
                    visited_fill(i,j,level,visited)
    max_area=max(max_area,area)
print(max_area)


