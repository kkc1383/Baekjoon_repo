import sys

num=int(sys.stdin.readline().strip())

num_list=[0]+list(map(int,sys.stdin.readline().strip().split()))

question_num=int(sys.stdin.readline().strip())

question_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(question_num)]

dp=[[False]*(num+1) for _ in range(num+1)] # dp[i][j]는 i부터 j까지가 팰린드롬인지

for i in range(1,num+1): # 길이가 1일때
    dp[i][i]=True

for i in range(1,num): # 길이가 2일때
    dp[i][i+1]=(num_list[i]==num_list[i+1])

for length in range(3,num+1): # 길이가 3이상일 때
    for i in range(1,num+1-length+1): 
        j=i+length-1 # i보다 length 갯수만큼 떨어진 곳 j
        dp[i][j]=(num_list[i]==num_list[j]) and dp[i+1][j-1] # 한 칸씩 내부의 dp를 보고 바깥만 체크하면 됨 dp의 기본 원리

for q_start,q_end in question_list:
    print(1 if dp[q_start][q_end] else 0)

# 이 문제는 어떻게 하면 팰린드롬 검사를 빠르게 할 수 있을지 생각해봐야하는 문제임
# dp테이블로 i~j가 팰린드롬인지 T,F 값을 저장한다. (사실상 답)
# 그리고 중요한 포인트는 뭐냐면 동적으로 생각했을 때 dp[i+1][j-1]이 팰린드롬이면 num_list[i]==num_list[j] 이것만 확인하면 애도 펠린드롬임을 알 수 있다.
# 이게 키 포인트였음