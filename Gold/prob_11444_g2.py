import sys

num=int(sys.stdin.readline().strip())
divide_num=1000000007
def multiple_matrix(matrixA,matrixB):
    new_matrix=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            new_matrix[i][j]=sum((matrixA[i][k]*matrixB[k][j])%divide_num for k in range(2))%divide_num
    return new_matrix


def fibo(n):
    base=[[1,1],[1,0]]
    # [[1,1],[1,0]]을 n제곱했을 때 (0,1)을 반환
    if n==1:
        return base
    else:
        if n%2==0: # 짝수일때
            half=fibo(n//2)
            base=multiple_matrix(half,half)
        else: # 홀수 일때
            base=multiple_matrix(base,fibo(n-1))
        return base

print(fibo(num)[0][1])

# 짝수일때 계산 두번 하지 않게 주의
# 피보나치의 수는 행렬의 제곱으로 나타낼 수 있다
# [[1,1],[1,0]]의 n제곱으로 나타나면 [[F(n+1),F(n)],[F(n),F(n-1)]] 로 나타낼 수 있다. 이 문제의 큰 착안점