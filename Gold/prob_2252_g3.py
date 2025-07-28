from collections import defaultdict, deque
import sys

human_num,comp_num=list(map(int,sys.stdin.readline().strip().split()))
comp_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(comp_num)]

adj_dict=defaultdict(list) # 준비물 1 인접한 노드들을 담는 딕셔너리

indegree=[0]*(human_num+1) # 준비물 2 각 인덱스의 진입차수를 담는 list

for s,e in comp_list: # 준비물 1,2를 만드는 과정
    adj_dict[s].append(e)
    indegree[e]+=1

# 1. 진입차수가 0인 노드를 큐에 집어 넣는다.
# 2. 큐에서 pop한 노드와 인접한 노드들의 진입차수를 1 감소한다.
# 3. 감소한 후에 진입차수가 0인 노드들을 큐에 집어 넣는다.
# 4. 2,3을 반복한다.

myqueue=deque()
result=[]
for start in range(1,human_num+1): # 우선 진입차수가 0인 노드를 전부 큐에 집어 넣습니다.
    if indegree[start]==0:
        myqueue.append(start)

while myqueue:
    top=myqueue.popleft()
    result.append(top)
    for e in adj_dict[top]:
        indegree[e]-=1
        if indegree[e]==0:
            myqueue.append(e)

print(*result, sep=" ")

# DFS로 푸는 방식도 있음