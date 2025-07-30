import sys
from collections import defaultdict, deque

adj_dict=defaultdict(list)

singer_num,case_num=list(map(int,sys.stdin.readline().strip().split()))
indegree=[0]*(singer_num+1)

for _ in range(case_num):
    line=list(map(int,sys.stdin.readline().strip().split()))
    for x in range(1,len(line)-1):
        if not line[x+1] in adj_dict[line[x]]:    
            adj_dict[line[x]].append(line[x+1])
            indegree[line[x+1]]+=1

myqueue=deque()
for i in range(1,singer_num+1):
    if indegree[i]==0:
        myqueue.append(i)
answer=[]
while myqueue:
    top=myqueue.popleft()
    answer.append(top)
    for next in adj_dict[top]:
        indegree[next]-=1
        if indegree[next]==0:
            myqueue.append(next)

if len(answer)!=singer_num:
    print(0)
else:
    print(*answer, sep="\n")

# 위상정렬을 사용하는 아주 기본적인 문제
# 트러블슈팅을 하자면 line에서 받아올떄 인덱스 관련 처리가 조금 미흡했음