import sys

n=int(sys.stdin.readline().rstrip())

step_list=[]
for _ in range(n):
    input_value=int(sys.stdin.readline().rstrip())
    step_list.append(input_value)

dp=[0]*n

try:
    dp[0]=step_list[0]
    dp[1]=step_list[1]+step_list[0] # 2번재 계단 까지의 최댓값이니까 더하는게 맞다
    dp[2]=max(step_list[0],step_list[1])+step_list[2]
except:
    pass

if n>3:
    for i in range(3,n):
        dp[i]=max(dp[i-2]+step_list[i],dp[i-3]+step_list[i-1]+step_list[i])
print(dp[n-1])


# 역시 dp 재귀는 시간이 너무 오래걸린다 이에 대한 해결책은 바텀업 dp 방식이다.
# 바텀업 dp 방식은 일단 초기값을 미리 설정 해두고 for문을 이용해 밑에서부터 천천히 올라가는 방식이며
# list에다가 해당 값들을 저장해가며 필요할때 써먹는 방식으로 감
# n==1일 경우 dp[2]를 참조를 못하니까 indexerror가 생기는데 어차피 사용하지도 않아서 그냥 try except구문 씀