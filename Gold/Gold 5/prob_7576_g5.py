from collections import deque
import sys

x_num,y_num=list(map(int,sys.stdin.readline().strip().split()))

done_tomato_list=[] # 다익은 토마토들의 (y,x) 의 list
no_tomato_count=0
map_tomato=[] # 전체 맵
for y in range(y_num):
    line=list(map(int,sys.stdin.readline().strip().split()))    
    for x in range(x_num):
        if line[x]==1:
            done_tomato_list.append((y,x))
        if line[x]==-1:
            no_tomato_count+=1
    map_tomato.append(line)


myqueue=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for done in done_tomato_list:
    myqueue.append(done)

daily_tomato=done_tomato_list
time=0
while True:
    if len(done_tomato_list)+no_tomato_count==x_num*y_num: # 다 익었으면
        print(time)
        break

    extra_tomato=[] # 그 날 익은 토마토들
    for tomato_y,tomato_x in daily_tomato: # 전날에 익은 토마토들이 주변 토마토를 익게 만드는 과정 (1일치)
        for k in range(4):
            new_y=tomato_y+dy[k]
            new_x=tomato_x+dx[k]
            if new_y>=y_num or new_y<0 or new_x>=x_num or new_x<0: # 범위를 벗어났으면 탈락
                continue
            if map_tomato[new_y][new_x]==0:
                extra_tomato.append((new_y,new_x))
                map_tomato[new_y][new_x]=1

    if not extra_tomato: # 하나도 익게하지 못하였다면
        print(-1)
        break

    time+=1
    daily_tomato=extra_tomato # 다음 루프에 돌 수 있도록 아까 익엇던 토마토들을 넘겨줌
    done_tomato_list.extend(extra_tomato) # 다 익은 토마토 리스트에 넣어줌

    
