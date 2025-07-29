from collections import deque
import sys

y_num,x_num=list(map(int,sys.stdin.readline().strip().split()))
water_list=set()
land_list=set()
rock_list=set()
dest=None
walk_list=set()
for y in range(y_num):
    line=list(sys.stdin.readline().strip())    # 붙어있는 문자열이라면 split 없애기
    for x in range(x_num):
        if line[x]=="D":
            dest=(y,x)
        elif line[x]=="S":
            walk_list.add((y,x))
        elif line[x]=="*":
            water_list.add((y,x))
        elif line[x]==".":
            land_list.add((y,x))
        elif line[x]=="X":
            rock_list.add((y,x))
    
dx=[1,-1,0,0]
dy=[0,0,1,-1]

time=0
visited=[[False]*x_num for _ in range(y_num)]
success=False
next_water=water_list
while True:
    # 다음 턴에 생길 물 좌표 계산
    extra_water=set()
    for water_y,water_x in next_water:
        for k in range(4):
            new_x=water_x+dx[k]
            new_y=water_y+dy[k]
            if new_x<0 or new_x>=x_num or new_y<0 or new_y>=y_num: # 맵 밖을 나가면
                continue
            if (new_y,new_x) in rock_list or (new_y,new_x)==dest or (new_y,new_x) in water_list: # 바위나 목적지가 있다면, 그리고 이미 water_list안에 있다면
                continue
            extra_water.add((new_y,new_x))
            land_list.discard((new_y,new_x))

    water_list.update(extra_water)
    next_water=extra_water
    time+=1
    # 너구리가 움직일 수 있는 방향 찾기
    extra_walk=set()
    for walk_y,walk_x in walk_list:
        for k in range(4):
            new_x=walk_x+dx[k]
            new_y=walk_y+dy[k]
            if (new_y,new_x) in land_list:
                if not (new_y,new_x) in extra_water:
                    extra_walk.add((new_y,new_x))
            elif (new_y,new_x)==dest:
                success=True
                break
        if success:
            break
    if success:
        print(time)
        break
    if not extra_walk:
        print("KAKTUS")
        break
    walk_list=extra_walk
    
# 진짜 인덱스 접근할거아니면 set쓰는게 사기다 탐색속도가 O(1)임