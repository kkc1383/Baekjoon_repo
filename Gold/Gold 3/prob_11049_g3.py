import sys

matrix_num=int(sys.stdin.readline().strip())

row_list=[]
col_list=[]

dims=[]

for i in range(matrix_num):
    row,col=list(map(int,sys.stdin.readline().strip().split()))
    if i==0:
        dims.append(row) # 처음에만 row를 append하고 나머지는 col 만 받음 왜냐면 현재 col과 다음 row가 겹치니까
    dims.append(col)

INF=float('inf')
dp=[[INF]*matrix_num for _ in range(matrix_num)]

for i in range(matrix_num): # 초기 dp 채워넣기
    for j in range(i,matrix_num):
        if i==j:
            dp[i][j]=0 # 같은건 0
        if j-i==1:
            dp[i][j]=dims[i]*dims[i+1]*dims[j+1] # 하나차이나는건 그냥 곱해주면 그만


for length in range(2,matrix_num+1): # 간격은 최소 2, 간격이 1이 되면 두개 그냥 연산값이랑 같아짐 m*k*n 그건 위에서 해줌
    for i in range(matrix_num-length): # 간격이 정해졌으니까 간격보다 max에서 떨어져야 하니까
        j= i+length # 정해진 간격만큼 떨어진 j
        for k in range(i,j): #여기서 k가 mid이고 여기서 길이 하나차이나는 것에 대해서 계산
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+dims[i]*dims[k+1]*dims[j+1])


print(dp[0][matrix_num-1])
