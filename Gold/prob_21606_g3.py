from collections import defaultdict
import sys

ver_num=int(sys.stdin.readline().strip())
inout_list=[0]+list(map(int,sys.stdin.readline().strip()))

adj_dict=defaultdict(list)

visited=[0]*(ver_num+1)
total_count=0
for _ in range(ver_num-1):
    a,b=tuple(map(int,sys.stdin.readline().strip().split()))
    if inout_list[a]==1 and inout_list[b]==1:
        total_count+=2
    else:
        adj_dict[a].append(b)
        adj_dict[b].append(a)

def dfs_iter(start,visited):
    stack=[start]
    permutation=set()
    while stack:
        top=stack.pop()
        for e in adj_dict[top]:
            if visited[e]==i: # 방문한 곳은 스택에 쌓지 않음
                continue
            visited[e]=i # 방문했다고 체크
            if inout_list[e]==1: # 끝이 실내라면 끝내야 함
                permutation.add(e)
            else: # 실외라면 다음을 향해
                stack.append(e)
    count=len(permutation)
    return count*(count-1)

for i in range(1,len(inout_list)):
    if inout_list[i]==0 and visited[i]==0: # 이게 키 포인트였던 것 같음. 
        visited[i]=i
        total_count+=dfs_iter(i,visited)

print(total_count)

# 실외 하나만 덩그러니 있는 경우까지 탐색을 해버려서 이것까지 잡아야 하나 생각을 했지만? 이때는 permutation 계산할때 걸러준다. k(k-1)인데 k=1이라...
# 사실 gpt가 stdin.buffer.readline을 쓰라고 하긴 했지만 사실 안해도 통과 됐음. 로직이 문제였던거지
# 그래서 키 포인트는 뭐였냐면 한번 방문한 실외 노드에 대해서는 다시 들어갈 필요가 없었던 것이었음.
# defaultdict도 써도되고 set도 써도됨