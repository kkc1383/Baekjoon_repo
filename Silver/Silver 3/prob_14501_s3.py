import sys

finish=int(sys.stdin.readline().strip())

meeting_list=[tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(finish)]

dp=[0]*30

for i,(duration,reward) in enumerate(meeting_list):
    dp[i]=max(dp[i],dp[i-1]) # 상담을 하지 않았을 수도 있기 때문에 옆으로 확장을 해줘야 함

    if i+duration<=finish:
        dp[i+duration]=max(dp[i+duration],dp[i]+reward)

print(max(dp[:finish+1]))