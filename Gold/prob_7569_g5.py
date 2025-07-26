from collections import deque
import sys

x_num,y_num,z_num=list(map(int,sys.stdin.readline().strip().split()))

tomato_map=[]# 전체 맵
tomato_list=[]# 안익은 토마토가 있는 좌표
done_tomato_list=[] # 익은 토마토가 있는 좌표
for z in range(z_num):
    tomato_y=[]
    for y in range(y_num):
        line=list(map(int,sys.stdin.readline().strip().split()))
        tomato_y.append(line)
        for x in line:
            if x==0:
                tomato_list.append((z,y,x))
            elif x==1:
                done_tomato_list.append((z,y,x))
    tomato_map.append(tomato_y)

time=0
if not done_tomato_list: # 애초에 모두 다 익어있으면
        print(0)
        pass
while True:
    # 토마토가 모두 익지 못하는 상황일 때
    # 토마토가 모두 다 익었을 때


    # 하루 지나고 맵 번화
    queue_tomato=deque()
    queue_tomato.append(done_tomato_list[0][0],done_tomato_list[0][1],done_tomato_list[0][2])
    visited=[[[False]*x_num for _1 in range(y_num)] for _2 in range(z_num)]
    visited=[done_tomato_list[0][0]][done_tomato_list[0][1]][done_tomato_list[0][2]]=True

    while queue_tomato:
        top_z,top_y,top_x=queue_tomato.popleft()
    