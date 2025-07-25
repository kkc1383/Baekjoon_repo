from collections import defaultdict, deque
import sys

y_num,x_num=list(map(int,sys.stdin.readline().strip().split()))
ice_map=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(y_num)]
ice_list=[]
for i in range(1,y_num-1):
    for j in range(1, x_num-1):
        if ice_map[i][j]!=0:
            ice_list.append((i,j))

time=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while True: # 1년당 1행동
    bunch=0
    visited_bunch=[[False for _1 in range(x_num)] for _2 in range(y_num)]
    
    # 덩어리 찾기
    for i,j in ice_list:
        if not visited_bunch[i][j]: # 방문하지 않았다면
            visited_bunch[i][j]=True
            bunch+=1
            find_queue=deque()
            find_queue.append((i,j))

            while find_queue:
                top=find_queue.popleft()
                for k in range(4):
                    x=top[1]+dx[k]
                    y=top[0]+dy[k]
                    if ice_map[y][x]!=0 and not visited_bunch[y][x]:
                        find_queue.append((y,x))
                        visited_bunch[y][x]=True
                            
    if bunch>1: # 덩어리가 둘로 나눠지면 그때 몇년인지 반환
        print(time)
        break
    if not ice_list:
        print(0)
        break
    time+=1
    # 맵 변화                        
    decay_map=[[0 for _1 in range(x_num)] for _2 in range(y_num)]
    for i,j in ice_list:
        for k in range(4): # 상하좌우를 돌면서
            x=j+dx[k]
            y=i+dy[k]
            if ice_map[y][x]==0: # 바다를 만나면
                decay_map[i][j]+=1
    new_ice_list=[]
    for i,j in ice_list:
        temp=ice_map[i][j]-decay_map[i][j]
        if temp>0:
            ice_map[i][j]=temp
            new_ice_list.append((i,j))
        else:
            ice_map[i][j]=0

    ice_list=new_ice_list

# 일단 문제를 이해하는 것이 중요 인접한 바다만큼 줄어드는 것이 문제였고
# 그다음 바다를일일이 줄이면 그다음 서칭때 원래 빙산이었는데 바다취급을 하는 문제가 발생할 수도 있음
# 시간초과가 나서 ice list를 만들어서 빙산 인것만 순회하도록 바꿈
# 그래서 0이 되서 침수된 곳은 icelist에서 빼주어야 함
# 그리고 icelist가 없어지면 0을 출력하고 빠져나가야함. <- 이게 중요했음