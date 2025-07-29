from collections import defaultdict, deque
import sys

city_num=int(sys.stdin.readline().strip())
road_num=int(sys.stdin.readline().strip())

adj_dict=defaultdict(list)
outdegree=[0]*(city_num+1)

for y in range(road_num):
    start, end, time=list(map(int,sys.stdin.readline().strip().split()))
    adj_dict[end].append((time,start)) # adj_dict[출발지점]=(걸리는시간, 도착점)
    outdegree[start]+=1

target_start,target_end=list(map(int,sys.stdin.readline().strip().split()))

time_dict=defaultdict(set)
max_time=0
myqueue=deque()
for elem in range(1,city_num+1):
    if outdegree[elem]==0:
        myqueue.append(elem)

while myqueue:
    top=myqueue.popleft()
    for e in adj_dict[top]:
        outdegree[e]-=1
        if outdegree[e]==0:
            myqueue.append(e)


# 일단 역방향으로 전출차수를 확인하고 장난감 조립 한것처럼 분해해나가면 될듯