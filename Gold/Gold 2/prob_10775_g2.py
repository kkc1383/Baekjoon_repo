import sys

gate_num=int(sys.stdin.readline().strip())
plane_num=int(sys.stdin.readline().strip())

gate_list=[int(sys.stdin.readline().strip()) for _ in range(plane_num)]

sum_plane=0

parent=list(range(gate_num+1))

def find(x):
    if x==0:
        return 0
    while x!=parent[x]:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x
for gate in gate_list:
    root=find(gate)
    if root==0:
        break
    else:
        sum_plane+=1
        parent[root]=find(root-1) # root에서 1을 빼주어야 제일 끝에 있는게 1빠져서 제대로 빠집니다. 뭐든 항상 root로 움직여야함 그게 바로 최신화 된 정보니까
print(sum_plane)
# 이 문제는 최소 스패닝 트리에서 배웠던 Union-find 를 사용합니다.
# 그래서 오른쪽부터 밀어넣는 방법을 손쉽게 구할 수 있습니다.
