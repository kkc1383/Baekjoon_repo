from collections import defaultdict, deque
import sys

toy_num=int(sys.stdin.readline().strip())
edge_num=int(sys.stdin.readline().strip())
edge_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(edge_num)]

adj_dict=defaultdict(list)

cnt=[defaultdict(int) for _ in range(toy_num+1)] # 객체라서 for로 복사해야함

indegree=[0]*(toy_num+1) # 위상정렬을 위한 진입차수 배열

for adv,basic,w in edge_list: # 인접배열 생성 및 진입차수 정립
    adj_dict[basic].append((adv,w))
    indegree[adv]+=1

basic_list=[]
for toy in range(1,toy_num+1): # 기본부품 list 생성
    if indegree[toy]==0:
        basic_list.append(toy) # 기본 부품들

basic_queue=deque() # 진입차수가 0인 기본부품들을 모두 queue에 넣는 작업
for basic in basic_list:
    cnt[basic][basic]=1
    basic_queue.append(basic)

while basic_queue: # 진입차수가 0인 부품부터 시작해서 인접노드들의 간선을 없애고 그럴때 진입차수가 0인 부품을 다시 넣는 방법 Kahn's algorithm
    top=basic_queue.popleft()
    for adv,w in adj_dict[top]:
        for key in cnt[top].keys(): # 중간부품을 만들기 위한 key 값에 완성을 위한 중간부품 갯수만큼 곱해주기
            cnt[adv][key]+=cnt[top][key]*w

        indegree[adv]-=1
        if indegree[adv]==0:
            basic_queue.append(adv)

result=[]

for key,value in cnt[toy_num].items():
    result.append((key,value))

result.sort()

for elem in result:
    print(f'{elem[0]} {elem[1]}')
        

# 처음에는 dfs로 풀릴 것 같아서 풀었고 로직은 맞는 것 같은데, 시간초과가남
# 모든 노드에 대해서 다 dfs를 돌리기 때문에 시간이 오래걸리는 거였음
# 그래서 위상정렬+dp를 사용하면 빠르게 풀리는데, 이는 간선의 가중치를 계속 누적시키면서 가니 한번의 순회만으로 결과가 나오는 것임
# 어떻게 하냐면 list(dict)를 사용하여 각 노드별 하위단계의 부품의 갯수를 dict에 차곡차곡 쌓는 것임.
# 여기서 시행착오 하나는 상위 단계의 dict에 최하위단계인 기본부품의 값을 넣어야 한다는 것. 그리고 애초에 곱해진 값 만큼 중간부품에 들어가있기 때문에 새로운 간선의 가중치만큼만 곱하면됨
# 그니까 예를 들어 중간부품 5는 기본1 2개, 기본2 두개가 있어서 cnt[5]={1:2,2:2}인데 완성부품 7을 만들기 위한 5를 계산할때 cnt[7]={1:2*2, 2;2*2} 이렇게 5->7 가중치만 곱하면 됨


# 개같이 시간초과 나버린 dfs 코드
# visited=[]

# def dfs(start,in_count):
#     count=0
#     visited[start]=True
#     if adj_dict[start]:
#         for e,w in adj_dict[start]:
#             count+=dfs(e,w*in_count)
#     else:
#         return in_count
#     return count

# print(basic_list)
# for basic in basic_list:
#     visited=[False]*(toy_num+1)
#     basic_count=dfs(basic,1)
#     print(f'{basic} {basic_count}')
