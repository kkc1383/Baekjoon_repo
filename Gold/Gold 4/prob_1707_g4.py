from collections import defaultdict
import sys

case_num=int(sys.stdin.readline().strip())  

for _ in range(case_num):
    ver_num,edge_num=list(map(int,sys.stdin.readline().strip().split()))
    edge_list=[list(map(int,sys.stdin.readline().strip().split())) for x in range(edge_num)]

    # BFS로 푸는 방법
    adj_dict=defaultdict(list)
    sys.setrecursionlimit(10**6)
    for s,e in edge_list:
        adj_dict[s].append(e)
        adj_dict[e].append(s)
    
    color_list=[-1]*(ver_num+1) #i번째 색 -1 미색칠, 0, 1 색칠
    illegal=False

    def dfs(ver,color): # color이 내 색깔 ver이 내 vertex
        global illegal
        color_list[ver]=color
        for v in adj_dict[ver]: # 인접해있는 모든 원소에 대해
            if color_list[v]==-1: # 안칠했으면
                dfs(v,1-color) # 내 색과 다른 색을 칠함
                if illegal:
                    return
            elif color_list[v]==color: # 이웃이 같은 색이면 모순 발생
                illegal=True
                return
    for node in range(1, ver_num+1):
        if color_list[node]==-1: # 색칠 안되있는거
            dfs(node,0) #스타트색은 그냥 0으로 통일 어짜피 안칠해져있는거 0으로 시작하면 밑에는 dfs돌면서 알아서 색칠됨
        if illegal:
            break
    print("YES" if not illegal else "NO")

    # DSU로 푸는 방법
    # parent=list(range(ver_num+1))
    # pairty=[0]*(ver_num+1) # 루트와 같은 색이면 0, 루트와 다른 색이면 1을 저장
    # rank=[0]*(ver_num+1)
    # def find(x):
    #     if parent[x]!=x:
    #         px=parent[x]
    #         parent[x]=find(px) # 한칸 앞 부모 인데 재귀라서 루트
    #         pairty[x]^=pairty[px] # 지금 루트랑 비교해서 같은거면 0 다른거면 1을 저장 같다 다르다의 상태를 나타내는 거임
    #     return parent[x]    
    # def union(x,y):
    #     rx,ry=find(x),find(y)
    #     if rx==ry:
    #         return (pairty[x]^pairty[y])==1 # 간선끼리인데 인접한 노드가 색이 같으면 모순이니까
    #     if rank[rx]>rank[ry]:
    #         parent[ry]=rx
    #         pairty[ry]=pairty[y]^pairty[x]^1
    #     elif rank[ry]>rank[rx]:
    #         parent[rx]=ry
    #         pairty[rx]=pairty[x]^pairty[y]^1
    #     else:
    #         parent[rx]=ry
    #         pairty[rx]=pairty[x]^pairty[y]^1
    #         rank[ry]+=1
    #     return True
    # illegal=False
    # for s,e in edge_list:
    #     if not union(s,e):
    #         illegal=True
    #         break
    # print("NO" if illegal else "YES")


# 이분 그래프임을 판별하려면 홀수 사이클일때 이분 그래프가 생기지 않기 때문에 0과 1의 색칠놀이로 사이클을 돌며 판별함