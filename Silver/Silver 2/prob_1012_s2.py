from collections import deque
import sys

test_case=int(sys.stdin.readline().strip())
for _1 in range(test_case):
    ver_num,hor_num,veg_num=list(map(int,sys.stdin.readline().strip().split()))
    veg_map=[[0]*(ver_num) for _ in range(hor_num)]

    veg_list=[]
    for _ in range(veg_num):
        x,y=list(map(int,sys.stdin.readline().strip().split()))
        veg_map[y][x]=1
        veg_list.append((y,x))


    myqueue=deque()

    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    visited=[[False]*(ver_num) for _ in range(hor_num)]
    count=0
    for veg_y,veg_x in veg_list: # 순회 할거고 bfs 거치면 visited로 걸러내기
        if visited[veg_y][veg_x]:
            continue
        myqueue.append((veg_y,veg_x))
        while myqueue:
            top_y,top_x=myqueue.popleft()
            for i in range(4):
                new_x=top_x+dx[i]
                new_y=top_y+dy[i]
                if new_x<0 or new_x>=ver_num or new_y<0 or new_y>=hor_num: # 맵을 벗어날 때
                    continue
                if not visited[new_y][new_x] and veg_map[new_y][new_x]==1: # 방문하지 않은 양배추 발견할 때
                    visited[new_y][new_x]=True
                    myqueue.append((new_y,new_x))
        count+=1

    print(count)

