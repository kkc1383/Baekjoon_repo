from collections import defaultdict, deque
import sys

vertex_num,edge_num,start_index=list(map(int,sys.stdin.readline().strip().split()))
edge_list=[tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(edge_num)]

adj=defaultdict(list)
for s,e in edge_list: # 양방향 그래프라서 양쪽을 다 넣어줌 key : 시작점, value: 갈 수 있는 지점들 list
    adj[s].append(e)
    adj[e].append(s)

for key in adj:
    adj[key].sort() # 여러 방향 갈 수 있다면 작은 방향부터 먼저 가야하기 때문에 정렬 해줌

visited_dfs=set() # 여기선 visited를 밖으로 빼놔야 함 재귀라서
def dfs(start): 
    visited_dfs.add(start) # 이제부터 들어갈 곳에 visited를 미리 해둠
    print(start,end=" ") # 할거니까 출력도해주고
    for e in adj[start]: # 갈 수 있는 곳을 다 갈겁니다.
        if not e in visited_dfs: # visited가 아니라면요
            dfs(e) # 재귀라서 계속 파고 들겁니다. 

# 만약 끝까지 갔다면 더이상 아무런 명령어를 실행하지 못하기 때문에 자동으로 빠져나가겠죠


def bfs(start): # deque

    # 초기값 설정, 초기 visited 만들고 deque 선언하고 시작지점 미리 집어넣고, 시작지점 visited 넣어두고
    visited_bfs=set() 
    bfs_deque=deque(start)
    visited_bfs.add(start)

    while bfs_deque: # deque가 없어질때까지
        top=bfs_deque.popleft() # 먼저 일거리 빼주고
        print(top, end=" ") # 어차피 일할거니까 print 해주고
        for e in adj[top]: # 그 일거리가 찾아올 다음 일거리들을 찾음
            if not e in visited_bfs: # 그 일거리들이 이미 한거면 넣지말고
                visited_bfs.add(e) # 어차피 들어갈거니까
                bfs_deque.append(e) # queue에 집어넣고

dfs(start_index)
print()
bfs(start_index)

# 여기서 키포인트는 dict를 만들어서 갈 수 있는 방향들을 정리해놓은 것, 리스트를 통해 시작지점을 가지고 가야하는 방향을 빠르게 찾아 낼 수 있었음. 리스트라면 일일이 탐색을 해야 했음
# 아니면 리스트를 bool list로 만들어서 index에 지점을 넣으면 visited를 했는지 안했는지 O(1)로 볼 수 있게끔
# 그리고 visited를 set으로 받아 놓는 것, 어짜피 중복안되니까 빠르게 접근 가능한 set을 쓰는게 낫다.