from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline().strip())
pair_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n-1)]

adj_dict=defaultdict(list)

for s,e in pair_list:
    adj_dict[s].append(e)
    adj_dict[e].append(s)

visited=[0]*(n+1)
def dfs(root,start):
    visited[start]=root
    for e in adj_dict[start]:
        if visited[e]==0:
            visited[e]=root
            dfs(start,e)

dfs(1,1)
for i in range(2,n+1):
    print(visited[i])

# 부모 찾기라고 해서 unionfind인줄알았지만, 그냥 dfs으로 풀 수 있는 문제였음... 어차피 함수끝나고 호출할 때 root로 돌아가니까 root 받아뒀다가 visited에 저장했음 그러면 자기 바로 위에 부모를 남기게 될것임
# 재귀니까용 backtrack하니까
