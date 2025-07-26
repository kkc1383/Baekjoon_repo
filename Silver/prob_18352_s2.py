from collections import defaultdict, deque
import sys

city_num,road_num,target,start=list(map(int,sys.stdin.readline().strip().split()))

road_dict=defaultdict(list)

for _ in range(road_num):
    s,e=list(map(int,sys.stdin.readline().strip().split()))
    road_dict[s].append(e) # 단방향이니까

length_list=[0]*(city_num+1) # 여기에 각 도시까지의 거리를 저장

visited=[False]*(city_num+1)
visited[1]=True
city_queue=deque()
city_queue.append(start)

while city_queue:
    top=city_queue.popleft()
    for e in road_dict[top]:
        if not visited[e]:
            visited[e]=True
            length_list[e]=length_list[top]+1
            city_queue.append(e)

result_list=[]
for i in range(len(length_list)):
    if length_list[i]==target:
        result_list.append(i)

print(*result_list, sep="\n") if result_list else print(-1)
# 삼항 연산자에는 컴프리헨션을 적을 수 없다.
# print(elem if result_list (for elem in result_list) else -1)가 아니라
# print(*result_list, sep="\n") if result_list else print(-1) 이 맞다. print 함수 자체를 양 옆에 두는 게 맞다


