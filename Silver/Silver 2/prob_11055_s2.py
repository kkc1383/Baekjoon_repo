import bisect
import sys


num=int(sys.stdin.readline().strip())

num_list=list(map(int,sys.stdin.readline().strip().split()))    


dp=num_list[:]
dp[0]=num_list[0]
for i,elem in enumerate(num_list):
    for j in range(i):
        if num_list[j]<elem:
            dp[i]=max(dp[i],dp[j]+num_list[i]) # 본인 자기자신이 클 수도 있으니 본인 자신도 max에 넣어둠 그리고 직전 원소까지의 dp값과 직전 원소를 합한것이 dp[i]의 후보 인것
    

print(max(dp))

# 스택이라 큰거 하나 들어오면 그다음 것들이 안들어옴 그래서 실제로 하나 하나 다더해야함
# 예를들어 1 10 3 4 5 이렇게 있으면 10이 뒤에꺼 다 막아서 못더하는 상황이 생김
# 그래서 dp로 풀어야함
