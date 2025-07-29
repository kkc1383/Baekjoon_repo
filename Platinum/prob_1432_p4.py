from collections import defaultdict, deque
import heapq
import sys

n=int(sys.stdin.readline().strip())

adj_dict=defaultdict(list)

outdegree=[0]*(n+1)
for y in range(n):
    input_line=list(map(int,sys.stdin.readline().strip()))
    for x in range(n):
        if input_line[x]==1:
            adj_dict[x+1].append(y+1)
            outdegree[y+1]+=1

max_heap=[]
for i in range(1,n+1):
    if outdegree[i]==0:
        heapq.heappush(max_heap,-i)

ans=[0]*(n+1)
label=n

while max_heap:
    top=-heapq.heappop(max_heap)
    ans[top]=label
    label-=1
    for e in adj_dict[top]:
        outdegree[e]-=1
        if outdegree[e]==0:
            heapq.heappush(max_heap,-e)

if 0 in ans[1:]:
    print(-1)
else:
    print(*ans[1:])

# 사이클이 생긴다는 것은 queue에 더이상 원소를 넣을 수 없는데 아직 남아있다는 말임
# 숫자가 작은게 안에 박혀 있고 그걸 찾아내려면 앞에서부터 박는게 아니라 거꾸로 뒤집어서 뒤에서부터 꺼내주면 성립한다.
# 무슨말이냐면 4와 5사이에 박힌 2를 꺼내야하기에 뒤에서부터 뿌시기 시작하면 5와 3에서 5를 먼저꺼내고 3과 2에서 3을 먼저 꺼내기 때문에 더이상 적수가 없을 경우 하는 수없이 맨 작은 수가 나오는 그런 로직
# 그래서 뒤에서부터 숫자가 큰것부터 밖으로 빼내면 된다.
# 그리고 인덱스 부여하는거는 어짜피 그래프 value랑 index랑 같으니까 진입차수가 큰 것중에 value가 큰것부터 차례로 뿌시기 시작하면 됨
# 그리고 사이클 검출은 순회하지 못한 노드가 있을 경우 이므로 방법은 여러가지겠지만 여기는 ans배열로 index를 기록했고 여기에 0이 하나라도 있다는 것은 순회를 안한 노드가 있다는 것이므로 사이클 검출