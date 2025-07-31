from collections import deque
import sys

y_num,x_num=list(map(int,sys.stdin.readline().strip().split()))

room_map=[list(sys.stdin.readline().strip()) for _ in range(y_num)]

answer=0
visited=[[False]*x_num for _ in range(y_num)]
for y in range(y_num):
    for x in range(x_num):
        if visited[y][x]:
            continue
        
        answer+=1

        tp= 1 if room_map[y][x]=="-" else 0 # tp는 타일의 종류이고 -이면 1 |이면 0
        myqueue=deque()
        myqueue.append((y,x,tp))
        
        while myqueue:
            top_y,top_x,top_tp=myqueue.popleft()
            if top_tp==0: # 세로이면:
                if top_y+1<y_num and not visited[top_y+1][top_x] and room_map[top_y+1][top_x]=="|": # 범위를 벗어나지 않고, 방문을 안 했고, 세로여야함
                    myqueue.append((top_y+1,top_x,top_tp))
                    visited[top_y+1][top_x]=True
            else:
                if top_x+1<x_num and not visited[top_y][top_x+1] and room_map[top_y][top_x+1]=="-": # 범위를 벗어나지 않고, 방문을 안 했고, 세로여야함
                    myqueue.append((top_y,top_x+1,top_tp))
                    visited[top_y][top_x+1]=True
print(answer)