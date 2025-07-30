from collections import defaultdict, deque
import sys

human_num,party_num=list(map(int,sys.stdin.readline().strip().split()))
truth_line=list(map(int,sys.stdin.readline().strip().split()))
truth_num=truth_line[0]
truth_set=set(truth_line[1:])
party_list=[]

adj_dict=defaultdict(list)
for _ in range(party_num):
    input_line=list(map(int,sys.stdin.readline().strip().split()))
    n=input_line[0]
    for x in range(1,len(input_line)-1):
        adj_dict[input_line[x]].append(input_line[x+1])
        adj_dict[input_line[x+1]].append(input_line[x])
    member=input_line[1:]
    party_list.append(member)
myqueue=deque(list(truth_set))
while myqueue: # 이걸로 전부 진실을 알게된 사람을 꿰뚫게 되었음
    top=myqueue.popleft()
    for next in adj_dict[top]:
        if not next in truth_set:
            truth_set.add(next)
            myqueue.append(next)

count=0
for party in party_list:
    if truth_set&set(party):# party에 진실을 아는 사람이 있다면
        continue
    count+=1

print(count)
# 무식하게 일단 거짓말쟁이들만 있는 파티는 전부다 dict에 집어 넣는다. dict[사람]+=1 이런식으로
# 그럼 그사람이 걸쳐있는 파티갯수가 있을 것이다.
# 그런다음에 진실된 사람이 들어가있는 파티 중 거짓말인 사람들만 set으로 모아가지고 dict에서 빼주면 될듯
# 이러면 중복해서 빠질텐데....
# 그래서 bfs를 통해서 진실을 알게될 사람을 미리 구하고 그 이후로 party갯수를 구함