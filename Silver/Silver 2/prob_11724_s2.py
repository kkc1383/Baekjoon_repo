import sys

vertex_num,edge_num=list(map(int,sys.stdin.readline().strip().split()))
parent=list(range(vertex_num+1))  # 표현식 외워두자!
rank=[0]*(vertex_num+1)

def find(parent,x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x

def union(parent,a,b):
    ra,rb=find(parent,a),find(parent,b)
    if ra==rb:
        return False
    if rank[ra]<rank[rb]:
        parent[ra]=rb
    elif rank[rb]<rank[ra]:
        parent[rb]=ra
    else:
        parent[rb]=ra
        rank[ra]+=1
    return True

for _ in range(edge_num):
    start,end=list(map(int,sys.stdin.readline().strip().split()))
    union(parent,start,end)

for i in range(1,vertex_num+1):
    find(parent,i) # 마지막에 싹 정리
parent_set=set(parent)
print(len(parent_set)-1)

# 두개가 연결이 되었음을 확인하는 방법은 union find 집합을 쓰는 것이다.
# 별로 고칠게 없네