from math import sqrt
import sys

num=int(sys.stdin.readline().rstrip())

def find(n):
    INF=10**9
    dp=[0]+[INF]*n
    for i in range(1,n+1):
        j=1
        while j**2<=i:
            dp[i]=min(dp[i],dp[i-j**2]+1)
            j+=1
    return dp[n]

print(find(num))

# 이 문제는 dynamic programming을 통해 풀 수 있다.
# 우리가 구하려는 dp[] a+b^2로 나타낼 수 있고 a에 대한 dp[a]는 로직상 이미 최선의 것이 구해져 있기 때문에
# 그것을 활용하여 최솟값을 찾는 것이다.
# 제곱수라는것이 사실 차이가 커서 무조건 가장 큰 수부터 쳐내려가면 될 것이라고 생각했는데 (그리디) 알고보니 예외가 있었던 것임
# 큰 문제 = 작은 문제 + 한 단계 라면 dp를 떠올리자