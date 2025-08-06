import sys

test_case=int(sys.stdin.readline().strip())

for _ in range(test_case):
    ver_num=int(sys.stdin.readline().strip())
    score_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(2)]

    dp=[[0]*(ver_num) for _ in range(2)]

    if ver_num==1:
        print(max(score_list[0][0],score_list[1][0]))
        continue
    dp[0][0]=score_list[0][0]
    dp[0][1]=score_list[0][1]+score_list[1][0]
    dp[1][0]=score_list[1][0]
    dp[1][1]=score_list[1][1]+score_list[0][0]
    for n in range(2,ver_num):
        dp[0][n]=max(dp[1][n-1], dp[1][n-2])+score_list[0][n]
        dp[1][n]=max(dp[0][n-1], dp[0][n-2])+score_list[1][n]
    
    print(max(dp[0][ver_num-1],dp[1][ver_num-1])) 

    # vernum값이 작을 수도 있기 때문에 그에 대한 조치도 취해야 한다.
    # 이 경우는 각 테스트케이스를 실행해야되기 때문에 continue를 사용해야한다. sys.exit(0)이 아니라
    # 그리고 dp의 경우 해당 스티커를 붙일 수 있는 경우는 결국 대각 아래와 대각아래 왼쪽 밖에 없습니다. 다른 경우들도 다 있지만 결국엔 다 이걸로 귀결됩니다.
    # 이런 문제를 풀때는 마지막 단계가 어딘지 생각해봅시다. 무조건 마지막단계는 여기를 거쳐야 하는구나, 그 격자에 최단 거리 구하기 같은 느낌으로