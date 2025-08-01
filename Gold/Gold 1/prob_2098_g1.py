
# top-down memoization
import sys

n=int(sys.stdin.readline().strip())

cost_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

INF=float('inf')
dp=[[-1]*(1<<n) for _ in range(n)]

def tsp(city,visited): # 현재 위치와 여태 방문한 곳을 넣으면 한 바퀴 다돌기까지 남은 비용
    if visited==(1<<n)-1: # 전부 다돌았으면
        return cost_list[city][0] if cost_list[city][0] else INF # 마지막 도시에서 다시 빽 하는 근데 바로가는 길이 없으면 out
    
    if dp[city][visited]!= -1: # dp는 항상 최종결정된 값만 저장하기 때문에 이미 정의된 값을 호출하는거면 그 값을 그냥 반환
        return dp[city][visited]
    
    min_cost=INF
    for next in range(n):
        if not visited & (1<<next) and cost_list[city][next]!=0: # 방문하지 않은 next 그리고 내 위치에서 다음 위치까지가 길이 뚫려 있다면
            min_cost=min(min_cost, tsp(next,visited|(1<<next))+cost_list[city][next]) # 거기를 간거랑 이미 기록된거랑 비교해서 최솟값
    
    dp[city][visited]=min_cost # 가장 최소를 가지는 값을 dp에 넣음
    return min_cost # 리턴값이 곧 dp값

print(tsp(0,1))

# dp는 난 city에있고 visited를 거쳤고, 한바퀴 다돌기에 남은 비용

# bottom-up dp 방식

import sys
input = sys.stdin.readline

n=int(sys.stdin.readline().strip())
cost_list = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

INF = float('inf')
dp = [[INF] * (1<<n) for _ in range(n)]
dp[0][1] = 0  # 시작도시 0, 방문상태 0...01  0번도시 방문완료
# 여기서 생각해볼것은 TSP문제는 출발지점이 크게 의미가 없다.
# 왜냐하면 예를들어 1->3->2->0->1이 정답 루트라고 하자, 그러면 3->2->0->1->3 도 답이고 2->0->1->3->2 도 답임.
# 결국 순환이기 때문에 어느 지점에서 시작해도 결과값은 같아짐 몇번째에 어딜 방문할지가 달라지는 것뿐 연속되는 순서는 같음

# dp 채우기
for mask in range(1<<n): # 모든 방문 상황에 대해서
    for cur_city in range(n): # 모든 지점에 대해 순회
        if not (mask & (1 << cur_city)): # 현재지점에서 모든 mask에 대해 순회할건데 현재지점이 방문처리가 안된 mask는 패스
            continue  
        for prev in range(n): # 이전에 밟고 있던 모든 prev에 대해서
            if (mask & (1 << prev)) and cost_list[prev][cur_city] != 0 and cur_city != prev: # mask가 방문 처리한 prev이고, prev에서 cur_city까지 길이 유효한지, cur_city와 prev가 같지 않은지 확인
                prev_mask = mask ^ (1 << cur_city) # cur_city를 방문하기 이전 mask
                dp[cur_city][mask] = min(dp[cur_city][mask], dp[prev][prev_mask] + cost_list[prev][cur_city]) # next를 방문하기 이전 최솟값에next로 

# 모든 도시 방문 후 0으로 돌아오는 비용 찾기
min_cost = INF
for last in range(1, n): # 다시 0번으로 돌아오는 경로가 있는 경우만
    if cost_list[last][0] != 0:
        min_cost = min(min_cost, dp[last][(1<<n)-1] + cost_list[last][0])
print(min_cost)