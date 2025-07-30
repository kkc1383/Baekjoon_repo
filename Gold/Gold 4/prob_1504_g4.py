from collections import defaultdict
import heapq
import sys

ver_num,edge_num=list(map(int,sys.stdin.readline().strip().split()))

adj_dict=defaultdict(list)
for _ in range(edge_num):
    start,end,cost=list(map(int,sys.stdin.readline().strip().split()))
    adj_dict[start].append((end,cost))
    adj_dict[end].append((start,cost))

ver1,ver2=list(map(int,sys.stdin.readline().strip().split()))


# start에 대해서
dist1=[float('inf')]*(ver_num+1) # 누적인데
myqueue=[]
dist1[1]=0
heapq.heappush(myqueue,(0,1)) # cost,node
 
while myqueue:
    top_cost,top=heapq.heappop(myqueue)
    if dist1[top]<top_cost:
        continue
    for next,cost in adj_dict[top]:
        new_time=dist1[top]+cost
        if dist1[next]<new_time:
            continue
        dist1[next]=new_time
        heapq.heappush(myqueue,(new_time,next)) # 힙에는 누적을 넣는다.

# ver1에 대해서
dist2=[float('inf')]*(ver_num+1) # 누적인데
myqueue=[]
dist2[ver1]=0
heapq.heappush(myqueue,(dist2[ver1],ver1)) # cost,node
while myqueue:
    top_cost,top=heapq.heappop(myqueue)
    if dist2[top]<top_cost:
        continue
    for next,cost in adj_dict[top]:
        new_time=dist2[top]+cost
        if dist2[next]<new_time:
            continue
        dist2[next]=new_time
        heapq.heappush(myqueue,(new_time,next)) # 힙에는 누적을 넣는다.

# ver2에 대해서
dist3=[float('inf')]*(ver_num+1) # 누적인데
myqueue=[]
dist3[ver2]=0
heapq.heappush(myqueue,(dist3[ver2],ver2)) # cost,node
while myqueue:
    top_cost,top=heapq.heappop(myqueue)
    if dist3[top]<top_cost:
        continue
    for next,cost in adj_dict[top]:
        new_time=dist3[top]+cost
        if dist3[next]<new_time:
            continue
        dist3[next]=new_time
        heapq.heappush(myqueue,(new_time,next)) # 힙에는 누적을 넣는다.

result=min(dist1[ver1]+dist2[ver2]+dist3[ver_num],dist1[ver2]+dist3[ver1]+dist2[ver_num])
if result==float('inf'):
    print(-1)
else:
    print(result)

# 특정 지점을 지나야한다면 예를 들어 v1,v2이라면
# start->v1 다익, v1->v2 다익, v2->end 까지 다익 돌리면 되지 않을까\
# 순서가 상관이 없었음 그래서 그 중의 최소를 구했어야 했는데
# start->v2가 될 수도 있다는 점
# 그래서 start->v1, start->v2를 모두 구하고
# v1->v2, v1->end를 구하고
# v2->v1, v2->end를 구한다음 조합별로 체크
# start->v1= dist1[ver1], start->v2 = dist1[ver2]
# v1->v2 = dist2[ver2] , v1-> end= dist2[ver_num]
# v2->v1 = dist3[ver1] , v2-> end= dist3[ver_num]
# 답은 누적으로 가지말고 따로따로 한 다음에 더하는 거