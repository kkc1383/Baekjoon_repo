from collections import deque
import sys

y_num,x_num=list(map(int,sys.stdin.readline().strip().split()))

campus=[]
doyeon=None
for y in range(y_num):
    line=list(sys.stdin.readline().strip())
    campus.append(line)
    for x in range(x_num):
        if line[x]=='I':
            doyeon=(y,x)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

myqueue=deque([doyeon])
visited=[[False]*(x_num) for _ in range(y_num)]
visited[doyeon[0]][doyeon[1]]=True
count=0
while myqueue:
    top_y,top_x=myqueue.popleft()
    # if visited[top_y][top_x]:
    #     continue
    # visited[top_y][top_x]=True
    for k in range(4):
        new_y=top_y+dy[k]
        new_x=top_x+dx[k]
        if new_y>=y_num or new_y<0 or new_x>=x_num or new_x<0 or campus[new_y][new_x]=="X":
            continue
        if visited[new_y][new_x]:
            continue
        visited[new_y][new_x]=True
        myqueue.append((new_y,new_x))
        if campus[new_y][new_x]=="P":
            count+=1

# print(campus)
print(count if count else "TT")

# visited처리를 언제하느냐가 중요한것 같음. 보통 맵 탐색할때는 뻗을때 visited 체크, 초기값 체크