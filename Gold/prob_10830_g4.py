import sys

n,b=list(map(int,sys.stdin.readline().rstrip().split()))

matrix=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def multiple(matrixA,matrixB):
    new_matrix=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j]=sum((matrixA[i][k]*matrixB[k][j])%1000 for k in range(n))%1000
    return new_matrix

def identity():
    new_matrix=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        new_matrix[i][i]=1
    return new_matrix

def divide(matrix,b):
    if b==0:
        return identity()
    else:
        if b%2>0:
            return multiple(matrix,divide(matrix,b-1))
        new_matrix=divide(matrix,b//2)
        return multiple(new_matrix,new_matrix)

for line in divide(matrix,b):
    print(' '.join(map(str,line)))


# 간단한 분할정복 문제임.
# 행렬의 곱을 표현하는걸 까먹어서 문제...
# 트러블 슈팅을 하자면 new_matrix=[[0]*n]*n의 식으로 초기화 해버리면 모든 행이 하나의 동일한 내부 리스트를 참조해서 어떤 원소를 바꾸면 그 열이 모든 행에서 동시에 바뀌어 버림
# 예를들어 new_matrix[1][1]에 값 2를 넣었다 치면 new_matrix[0][1]에도, new_matrix[2][1]에도 다 2로 바뀐다. 각 줄마다 참조하는 값이 같아버림.
# 그리고 또 한가지, 배열의 원소를 띄어쓰기 하나로 구분해서 프린트 하고 싶으면 print(' '.join(map(str,line))) 이와 같이 쓰면됨 map함수가 list를 str형태로 바꾸어주고 join함수로 사이사이에 공백을 넣음
