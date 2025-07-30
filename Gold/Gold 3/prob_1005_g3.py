from collections import defaultdict, deque
import heapq
import sys

test_case=int(sys.stdin.readline().strip())

for _1 in range(test_case):
    build_num, edge_num=list(map(int,sys.stdin.readline().strip().split()))
    time_list=[0]+list(map(int,sys.stdin.readline().strip().split()))
    edge_list=[list(map(int,sys.stdin.readline().strip().split())) for _2 in range(edge_num)]
    target=int(sys.stdin.readline().strip())

    adj_dict=defaultdict(list)
    indegree=[0]*(build_num+1)
    for s,e in edge_list:
        adj_dict[s].append(e)
        indegree[e]+=1
    
    dp=[0]*(build_num+1) # 누적
    base_list=[]
    for i in range(1,build_num+1): # 기본건물들 찾아서
        if indegree[i]==0:
            dp[i]=time_list[i] # dp에 미리 더해주고
            base_list.append(i) # 기본건물 리스트 만들어줘서 큐에 처음에 넣어줌
            
    myqueue=deque(base_list)

    while myqueue:
        top=myqueue.popleft()
        if top==target:
            break
        for next in adj_dict[top]:
            if dp[next]<dp[top]+time_list[next]: # 이게 포인트가 아닐까 싶은데
                dp[next]=dp[top]+time_list[next]
            indegree[next]-=1
            if indegree[next]==0:
                myqueue.append(next)
    print(dp[target])

# 분기가 나누어지는부분은 어떻게 해야할지 고민이었는데, 한 노드 한 노드가 각각 최대를 갱신해나가면 결국 합쳐지는 곳도 최대가 될 것이고 그게 곧 답이다.
# 그냥 위상정렬 해가면서 각 노드별 가질 수 있는 최대 누적값만 갱신해 나가면 됨.
# 그래서 포인트는 time_list(시간 배열)와 dp(누적시간)을 따로 두는 것이고 dp를 time_list에서 카피해와서 
# 처음에 dp를 cost로 카피해오는 이유는 기본 건물들의 시간을 더해줘야하기 때문이라고 생각하면 된다.
# 사실 로직은 다 상관없는데 그러면 기본 건물들이 마지막에 더해져야 한다.그리고 기본건물이 여러개일 경우 그 경쟁을 if문에서 해야하는데 그것조차 하기 힘들어진다.
    
