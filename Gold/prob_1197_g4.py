import sys

V,E=list(map(int,sys.stdin.readline().strip().split()))

def find(parent, x): # 루트 찾는 메소드
    while parent[x] !=x: # 이미 병합이 되어서 본인과 다른 거라면, 여기서 parent[x] x의 루트 인덱스
        parent[x]=parent[parent[x]] # 루트가 자기 자신을 루트로 하고 있다면 (루트라면)
        x=parent[x] # x에 루트인덱스를 저장
    return x # 루트 인덱스 반환

def union(parent, rank, a, b):   # 두개의 트리를 병합하는 메소드
    ra, rb=find(parent,a), find(parent, b)
    if ra==rb: # 사이클이 형성 되어버리는 케이스기 때문에 false
        return False
    if rank[ra]<rank[rb]: # rank 즉 노드 깊이가 깊은 쪽으로 붙게끔. 그게 연산이 적게 듬
        parent[ra]=rb # 족장 교체
    elif rank[ra]>rank[rb]:
        parent[rb]=ra
    else: 
        parent[rb]=ra # rank가 같은 경우인데 솔직히 아무나 해도 상관없긴함.
        rank[ra]+=1
    return True
# 여기서 rank가 높은 경우에 붙였을때 왜 rank를 올리지 않느냐면
# 어짜피 rank라는건 tree의 높이이고, 이는 1이상은 차이가 안난단 말이죠?
# 그러면 최소 차이가 1이라는건데 어짜피 tree를 이어붙이면 바로 아래에 붙일거라 높이차이가 나지 않습니다.
# 높이가 높은것에 붙이는 이유도 이거구요 높이 변화가 없으니깐

edges=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])

parent=list(range(V+1))
rank=[0]*(V+1)
mst_cost=0
picked=0

for u,v,w in edges:  # 이렇게 리스트의 원소를 한번에 접근할 수 있음
    if union(parent, rank, u ,v): # 사이클이 아니라면
        mst_cost+=w # 해당 간선을 채택했으니 cost에 저장해놓고
        picked+=1 # 간선 뽑은 횟수만큼 저장
        if picked==V-1: # 간선이 v-1만큼 뽑앗으면 다 뽑았네요
            break
print(mst_cost)

# 최소 스패닝 트리는 가장 큰 간선 하나만 뺀다고 되는 문제가 아님. 서로가 연결되어있는 연결성을 끊어버리면 안 됨
# 최소 스패닝 트리 문제는 크루스칼 알고리즘을 통해서 풀 수 있는데 이걸 알려면 unionfind 자료구조를 알아야함(상호 배타적 자료구조)
# 이를 공부할 수 있는 가장 기초적인 문제입니다.