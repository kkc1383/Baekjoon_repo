import sys

num=int(sys.stdin.readline().strip())


dp_max=[0]*3
dp_min=[0]*3

num_list_row=list(map(int,sys.stdin.readline().strip().split()))
for n in range(3):
    dp_max[n]=num_list_row[n]
    dp_min[n]=num_list_row[n]

for _ in range(1,num): # 각 줄 데이터를 그때 그때 받아가지고 한 줄씩 계산함
    
    num_list_row=list(map(int,sys.stdin.readline().strip().split()))

    new_dp_max=[0]*3
    new_dp_max[0]=max(dp_max[0],dp_max[1])+num_list_row[0]
    new_dp_max[1]=max(dp_max[0],dp_max[1],dp_max[2])+num_list_row[1]
    new_dp_max[2]=max(dp_max[1],dp_max[2])+num_list_row[2]
    dp_max=new_dp_max[:]
    
    new_dp_min=[0]*3
    new_dp_min[0]=min(dp_min[0],dp_min[1])+num_list_row[0]
    new_dp_min[1]=min(dp_min[0],dp_min[1],dp_min[2])+num_list_row[1]
    new_dp_min[2]=min(dp_min[1],dp_min[2])+num_list_row[2]
    dp_min=new_dp_min[:]

print(f'{max(dp_max)} {min(dp_min)}')

# dp 테이블 을 최댓값, 최솟값을 나눠서 2개 만들었더니 메모리초과가남
# 이 경우는 이전 행의 값만 필요하지 더 이전행들의 값은 필요가 없기 떄문에 n*n이 아니라 n의 1차원 배열만으로도 해결할 수 있음
# 이전 값들만 가지고 계산하고 그 값을 그대로 다음 행 연산에 쓸 수 있게 물려 주면됨 (슬라이딩 윈도우 기법)
# 이젠 입력 테이블조차도 메모리 초과가 나서 그냥 한줄 계산할때마다 한줄씩 받는걸로 고쳤음