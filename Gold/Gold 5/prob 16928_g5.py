from collections import deque
import sys

ladder_num, snake_num= list(map(int,sys.stdin.readline().strip().split()))

ladder_dict={start:end for start, end in (map(int,sys.stdin.readline().strip().split()) for _ in range(ladder_num))} # (~ 에서 , ~ 으로) 칸 올라가기
snake_dict={start:end for start, end in (map(int,sys.stdin.readline().strip().split()) for _ in range(snake_num))} # (~에서, ~으로 ) 칸 내려가기


myqueue=deque([1])
dist=[float('inf')]*(110)
dist[1]=0
while myqueue:
    top=myqueue.popleft()
    if top in ladder_dict: # 사다리를 밟았으면
        next=ladder_dict[top]
    elif top in snake_dict: # 뱀을 밟았으면
        next=snake_dict[top]
    else: # 아무것도 아니면
        next=top

    dist[next]=dist[top] # 사다리, 뱀 타고 이동한 곳도 같은 것

    if next==100:
        print(dist[next])
        break

    for i in range(1,7): # 다음 갈 수 있는 칸
        if dist[next+i]!=float('inf') or next+i>100:
            continue
        myqueue.append(next+i)
        dist[next+i]=dist[next]+1

# 주사위 굴려서 갈 수 있는 칸에다가 현재 dist[]+1 해서 계속 반복해나감 dp지
# dp를 쓸 수 없음.. 왔다갔다를 하기 때문에
# 대신에 중복제거만 하면 되지 싶음
# 1부터 시작이었음 1을 0으로하고 1만 넣고 시작하면됨