from collections import defaultdict, deque
import heapq
import sys

city_num=int(sys.stdin.readline().strip())
bus_num=int(sys.stdin.readline().strip())   

adj_dict=defaultdict(list)

for _ in range(bus_num):
    start,end,cost=list(map(int,sys.stdin.readline().strip().split()))
    adj_dict[start].append((end,cost)) # 일단 단방향이라고 생각하고

target_start,target_end=list(map(int,sys.stdin.readline().strip().split()))

cost_list=[10**15]*(city_num+1) # 각 CITY를 방문할때마다 걸리는 COST 이는 minimun으로 최신화 할 필요가 있음 그래서 다익스트라 씁니다.

bus_queue=[] # (그 정점까지 갈 때 드는 cost, 정점)
heapq.heappush(bus_queue,(0,target_start))  
cost_list[target_start]=0

while bus_queue:
    top_cost,top_vertex=heapq.heappop(bus_queue) # queue에 있는 원소중 비용이가장 작은 vertex뽑음
    if cost_list[top_vertex]<top_cost: # 내가 큐에서 뽑은 top까지 가는 거리가 이미 최신화된 top까지 가는 거리보다 더 멀 때 최신화 안된 버전이므로 pass
        continue # 최신화 정보인지, 구 정보인지 확인하는 절차
    for end,cost in adj_dict[top_vertex]:
        new_cost=cost_list[top_vertex]+cost
        if new_cost<cost_list[end]: # 사전에 알고 있던 최단 거리보다 내가 방금 만든 거리가 더 작으면 최신화
            cost_list[end]=new_cost
            heapq.heappush(bus_queue,(new_cost,end))   # 내가 개척해낸 새로운 정점이니까 다시 개척 해나가야지

print(cost_list[target_end])

# 가중치가 있는 그래프의 최단 비용은 다익스트라로 해결하면됨
# 다익스트라란 출발지점이 정해졌을 때 최소 비용인 길부터 택하는 것임. (우선순위 큐를 사용하여)