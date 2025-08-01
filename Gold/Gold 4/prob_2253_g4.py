from math import sqrt
import sys

target,cannot_num=list(map(int,sys.stdin.readline().strip().split()))

cannot_set=set(int(sys.stdin.readline().strip()) for _ in range(cannot_num))

jump_max=int(sqrt(2*target))+1 # 최대로 뛸수 있는 범위
dp=[[float('inf')]*(jump_max+2) for _ in range(target+1)] # dp[stone][jump_dist] stone까지 jump_dist로 갔을 때 최소 비용

dp[1][0]=0 # 초기값 중요함
for cur in range(2,target+1): # 어디에 도착했는지
    if cur in cannot_set:
        continue
    for jumped in range(1,jump_max+1):# 몇칸 앞으로 뛰었어서 왔는지
        if cur-jumped<1:
            break
        dp[cur][jumped]=min(dp[cur-jumped][jumped+1],dp[cur-jumped][jumped],dp[cur-jumped][jumped-1])+1

# print(*dp,sep="\n")
result=min(dp[target])
print(result if result!=float('inf') else -1)

# 점프를 먼저 순회하고 그다음 cur을 순회해야한다는데 이걸 결정하는 방법
# 점화식에서 cur-jumped는 고정인데 jumped는 -1,0,+1을 함 그런데 jumped를 외부로 해버리면 jumped+1이 정의가 안되는 문제가 있음
# 따라서 점화식에서 변화하는걸 체크하고 혹시 그 넘어서를 체크해야하는 경우 걔 먼저 순회 여기에선 jumped