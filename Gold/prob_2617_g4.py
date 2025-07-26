from collections import defaultdict
import sys

ball_num,edge_num=list(map(int,sys.stdin.readline().strip().split()))
edge_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(edge_num)]

adj_dict=defaultdict(list)

for large,small in edge_list: # 더 작은 공으로 가는 edge는 앞에 S, 더 큰 공으로 가는 edge는 앞에 L이 붙음
    if large!=small:
        adj_dict[large].append(('S',small))
        adj_dict[small].append(('L',large))

large_list=[0]*(ball_num+1) # index 공 , value 나보다 큰 공의 갯수
small_list=[0]*(ball_num+1) # index 공, value 나보다 작은 공의 갯수
result_list=[0]*(ball_num+1) # 각공의 large,small 중 가장 큰 값을 저장함 -> 이걸로 중간값이 안됨의 여부를 판단
limit_num=(ball_num//2)+1 # limit_num만큼 있어야 중간값 탈출 가능
count=0

for i in range(1,ball_num+1): # 각 공에 대해 순회 # dfs를 작은 공들에 대해서, 큰공들에 대해서 각각 해야 하기때문에 2번 실시

    visited_large=[False]*(ball_num+1)
    visited_large[i]=True
    large_stack=[i]

    while large_stack: # 나보다 큰 공들에 대해서 갯수 확인
        top=large_stack.pop()
        for SorL, next in adj_dict[top]:
            if SorL=="L" and not visited_large[next]:
                visited_large[next]=True
                large_stack.append(next)
                large_list[i]+=1

    if large_list[i]>=limit_num:
        count+=1
        continue

    visited_small=[False]*(ball_num+1)
    visited_small[i]=True
    small_stack=[i]

    while small_stack: # 나보다 작은 공들에 대해서 갯수 확인
        top=small_stack.pop()
        for SorL, next in adj_dict[top]:
            if SorL=="S" and not visited_small[next]:
                visited_small[next]=True
                small_stack.append(next)
                small_list[i]+=1

    if small_list[i]>=limit_num:
        count+=1
        continue

print(count)

# 왜 되지? stack으로 dfs 탐색할때 L만 보고싶을 때 S에 대해서 visited를 해버리면 틀리고 visited를 안하면 통과네
# 알았다 알았다. dfs 다 보니까 자식이 다른 후보군에 대해서 대소관계를 가지고 있을 때 지맘대로 visited를 해버림
# 무슨 말이냐면 4보다 작은게 2,3이 있어 그런데 3이 2보다 크대 그러면 4에서 시작해서 2로 들어갈건데 2에서 3을 visited처리를 해버린거지, 간선이 있으니까
# 그래서 내려갈 부분만 visited처리를 해야하고 안그런거에 대해선 건드리면 안됨, 그게 루트의 후보군일수도 있으니까