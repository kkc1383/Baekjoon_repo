import sys

test_case=int(sys.stdin.readline().strip()) 

for _ in range(test_case):
    coin_num=int(sys.stdin.readline().strip())
    coin_list=list(map(int,sys.stdin.readline().strip().split()))    
    target=int(sys.stdin.readline().strip())
    dp=[0]*(target+1)
    dp[0]=1 # 이거 중요 초기에 아무것도 안 담는 것도 경우임
    coin_list.sort() # 코인이 작은 것부터 시작해야 하기때문에, 문제 상황상 굳이 안해도 될 거 같음
    
    for coin in coin_list: # 작은 코인부터 시작해서 담아 나갈거기 떄문에 (왜냐하면 간격이 더 좁기 때문에)
        for i in range(coin,target+1): # 특정 코인 하나가 만들어 낼 수 있는 경우의 수들을 더함
            dp[i]+=dp[i-coin] # 내가 5원을 계산할거면 총 5원은 0원에서 , 6원은 1원에서 ~~
    print(dp[target])

