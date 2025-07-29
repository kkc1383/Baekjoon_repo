from collections import defaultdict, deque
import sys

city_num=int(sys.stdin.readline().strip())
road_num=int(sys.stdin.readline().strip())

forward_dict=defaultdict(list)
reverse_dict=defaultdict(list)
indegree=[0]*(city_num+1)

for _ in range(road_num):
    start,end,time=list(map(int,sys.stdin.readline().strip().split()))
    forward_dict[start].append((end,time))
    reverse_dict[end].append((start,time))
    indegree[end]+=1

target_start,target_end=list(map(int,sys.stdin.readline().strip().split()))
time=[0]*(city_num+1)
myqueue=deque([target_start])

while myqueue:
    top=myqueue.popleft()
    for next,next_time in forward_dict[top]:
        if time[next]<time[top]+next_time:
            time[next]=time[top]+next_time
        indegree[next]-=1
        if indegree[next]==0:
            myqueue.append(next)

visited_edge=set()
critical_edge=0
myqueue=deque([target_end])
visited_node=[False]*(city_num+1)
visited_node[target_end]=True

while myqueue:
    top=myqueue.popleft()
    for prev,prev_time in reverse_dict[top]:
        if time[top]==time[prev]+prev_time:
            if (prev,top) not in visited_edge:
                visited_edge.add((prev,top))
                critical_edge+=1
            if not visited_node[prev]: # 모든 행동을 위의 조건을 만족한 상태에만 제공합니다.
                visited_node[prev]=True
                myqueue.append(prev)

print(time[target_end])
print(critical_edge)



# 일단 역방향으로 전출차수를 확인하고 장난감 조립 한것처럼 분해해나가면 될듯
# 지금 뭐가 문제냐면 작은게 나오면 지워야 하고 같은게 나오면 남겨야 하는데 그것을 어찌 알리
# set이 오버헤드가 큼
# 최장거리와 그 길찾는것을 따로 하는 것도 방법임.

# 이 문제를 푸는데 키 포인트는 메모리, 시간 초과 없이 해결하는 것임
# 역방향 bfs란 다 되어 있는 밥에 조건을 걸어서 조건에 만족하는 것만 돌돌돌 말아 들어오는 것임
# 