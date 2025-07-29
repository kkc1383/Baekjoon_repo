from collections import deque
import sys

n=int(sys.stdin.readline().strip())
maze=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
dist=[[10**15 for _x in range(n)] for _y in range(n)]
room_queue=deque()
room_queue.append((0,0,0))
dist[0][0]=0
dx=(-1,1,0,0)
dy=(0,0,-1,1)

while room_queue:
    top_y,top_x,top_count=room_queue.popleft()
    for k in range(4):
        next_x=top_x+dx[k]
        next_y=top_y+dy[k]
        if 0<=next_x<n and 0<=next_y<n:
            isBlack= (maze[next_y][next_x]==0)
            if dist[next_y][next_x]>dist[top_y][top_x]+isBlack: # 내가 직접만든 다음칸의 비용이 이미알려진 다음칸의 비용보다 작을 경우 최신화 해야겠지?
                dist[next_y][next_x]=dist[top_y][top_x]+isBlack # dist배열에 최솟값 최신화
                if not isBlack: # 흰방들을 먼저 우선예약 해줌( 다익스트라의 비용이 가장적은 노드부터 순회하는 개념을 deque로 표현 한 것임 어짜피 0과 1의 관계여서)
                    room_queue.appendleft((next_y,next_x,dist[next_y][next_x]))
                else:
                    room_queue.append((next_y,next_x,dist[next_y][next_x]))


print(dist[n-1][n-1])

# 이제 왜 검은 방은 appendleft를 하느냐 를 알아야 할듯 사실 흰방이 appendleft이자 우선예약으로 빠르게 탐색을 마무리 하려고 하는 것임.
# 일단 가중치가 따로 없고 0과 1로 만존재하기 때문에 0-1 BFS로 접근 하면됨!
# 빠르게 탐색을 마치고 이제 차례로 벽을 넘어 가는데 이때 벽에 대해 최소 값이 넘어가도록 함.
# 각 흰 방에 대해서 벽을 넘은 값들이 쫙 퍼지게 될텐데. 각 벽의 숫자로 쫙 물들이는거임. 그걸 벽 블록 만큼 하는거고 그래서 둘러싸고 있는 벽들에 의해 다 색칠되면 결국 가장 낮은 비용만 남게될 것이고 이를 반복하는거임
