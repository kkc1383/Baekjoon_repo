from collections import deque
import sys

y_num,x_num=list(map(int,sys.stdin.readline().strip().split()))

maze=[list(map(int,sys.stdin.readline().strip())) for _ in range(y_num)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
# 인접노드는 map으로 판단할거라 건너뛰고 map에 그리는걸로
def bfs(start_x,start_y):
    visited=[[False for _x in range(x_num)] for _y in range(y_num)]
    visited[start_y][start_x]=True
    map_queue=deque()
    map_queue.append((start_y,start_x))

    while map_queue:
        top=map_queue.popleft()
        for i in range(4):
            new_x=top[1]+dx[i]
            new_y=top[0]+dy[i]
            if new_x>=0 and new_x<x_num and new_y>=0 and new_y<y_num: # 맵 밖을 벗어나지 않는 선에서
                if maze[new_y][new_x]!=0 and not visited[new_y][new_x]: # 벽이 아니고, 방문하지 않은 칸에 대해
                    map_queue.append((new_y,new_x))
                    visited[new_y][new_x]=True
                    maze[new_y][new_x]=maze[top[0]][top[1]]+1

bfs(0,0)
print(maze[y_num-1][x_num-1])

## 제발 큐면 popleft조심하자 이거 매번 햇갈려
# 그리고 bfs니까 최소 거리가 무조건 생기는거임 그래서 갈때마다 다 visited 걸어도 됨 한번만 가는게 맞다 이말이야