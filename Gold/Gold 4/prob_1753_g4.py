from collections import defaultdict
import heapq
import sys

ver_num,edge_num=list(map(int,sys.stdin.readline().strip().split()))
target_start=int(sys.stdin.readline().strip())
adj_dict=defaultdict(list)

for _ in range(edge_num):
    start,end,cost=list(map(int,sys.stdin.readline().strip().split()))
    adj_dict[start].append((end,cost))

cost_list=[float('inf')]*(ver_num+1)
cost_list[target_start]=0
myqueue=[]
heapq.heappush(myqueue,(0,target_start))

while myqueue:
    top_cost,top=heapq.heappop(myqueue)
    if cost_list[top]<top_cost:
        continue
    for next,cost in adj_dict[top]:
        if cost_list[next]>cost_list[top]+cost:
            cost_list[next]=cost_list[top]+cost
            heapq.heappush(myqueue,(cost_list[next],next))
for i in range(1,ver_num+1):
    print(cost_list[i] if cost_list[i]!=float('inf') else "INF")

# 변수이름 혼용하지 않도록 조심합시다.
# 시작지점 start랑 adjdict 채우는 start랑 혼용되었음