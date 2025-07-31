
from collections import defaultdict, deque
import heapq
import sys

n, virus_num=list(map(int,sys.stdin.readline().strip().split()))

virus_dict=defaultdict(list)
map_virus=[]
no_virus_count=0
for y in range(n):
    line=list(map(int,sys.stdin.readline().strip().split()))

    for x in range(n):
        if line[x]!=0:
            virus_dict[line[x]].append((y,x))
        else:
            no_virus_count+=1

    map_virus.append(line)

target_time, target_y, target_x=list(map(int,sys.stdin.readline().strip().split()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(target_time):
    for virus in range(1,virus_num+1): # 바이러스가 작은것부터 먼저

        myqueue=deque()
        for _y,_x in virus_dict[virus]: # 해당 바이러스가 있는 좌표를 큐에 넣음 , 나중에는 그 전 초에 감염시킨 좌표들만 남음
            myqueue.append((_y,_x)) 
        
        extra_virus=[] # 해당 초에 새로 감염시킨 좌표들
        while myqueue:
            top_y,top_x=myqueue.popleft()

            for k in range(4):
                new_y=top_y+dy[k]
                new_x=top_x+dx[k]
                if new_y>=n or new_y<0 or new_x>=n or new_x<0 : # 맵을 벗어날 경우 CONTINUE
                    continue
                if map_virus[new_y][new_x]==0: # 감염이 안된 곳
                    map_virus[new_y][new_x]=virus
                    extra_virus.append((new_y,new_x))
                    no_virus_count-=1
        virus_dict[virus]=extra_virus[:]
    
    if no_virus_count==0:
        break

print(map_virus[target_y-1][target_x-1])
