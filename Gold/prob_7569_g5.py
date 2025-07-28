from collections import deque
import sys

x_num,y_num,z_num=list(map(int,sys.stdin.readline().strip().split()))
not_ripe_count=0
tomato_map=[] # 전체 맵
done_tomato_list=[] # 익은 토마토가 있는 좌표
for z in range(z_num):
    tomato_y=[]
    for y in range(y_num):
        line=list(map(int,sys.stdin.readline().strip().split()))
        tomato_y.append(line)
        for x in range(x_num):
            if line[x]==1:
                done_tomato_list.append((z,y,x))
            elif line[x]==0:
                not_ripe_count+=1
    tomato_map.append(tomato_y)

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,-1,1]

time=0
if not_ripe_count==0: # 애초에 모두 다 익어있으면
    print(0)

else:

    while True:
        # # 하루 지나고 맵 번화
        extra_tomato=[]
        for tomato in done_tomato_list:
            for k in range(6): # 상하좌우왼오를 보고 결정
                new_z=tomato[0]+dz[k]
                new_y=tomato[1]+dy[k]
                new_x=tomato[2]+dx[k]
                if new_x>=x_num or new_x<0 or new_y>=y_num or new_y<0 or new_z>=z_num or new_z<0:
                    continue
                if tomato_map[new_z][new_y][new_x]==0: # 안익은 토마토라면
                    tomato_map[new_z][new_y][new_x]=1
                    extra_tomato.append((new_z,new_y,new_x))
                    not_ripe_count-=1

        done_tomato_list=extra_tomato # 여기가 포인트 그날 익은 것만 순회!

        if not extra_tomato: # 변화가 없으면
            print(-1)
            break

        time+=1         
        if not_ripe_count==0: # 안익은 토마토가 없을 경우
            print(time)
            break

# 모든 익은 토마토를 다 순회하면 시간이 오래걸림
# 따라서 그날 익었던 토마토만 돌면 될 것 같음