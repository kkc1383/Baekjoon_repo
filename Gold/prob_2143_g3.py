import sys
from typing import Counter

T=int(sys.stdin.readline().strip())
A_num=int(sys.stdin.readline().strip())
A_list=list(map(int,sys.stdin.readline().strip().split()))
B_num=int(sys.stdin.readline().strip())
B_list=list(map(int,sys.stdin.readline().strip().split()))

def get_all_sum(arr):
    partial_sums=[]
    for i in range(len(arr)): # 기준으로 이거랑 오른쪽으로 하나씩 더한 값마다 다 append
        total=0
        for j in range(i,len(arr)):
            total+=arr[j] # 이부분이네, arr[0] append, arr[0]+arr[1], append
            partial_sums.append(total)
    return partial_sums # 중복도 당연히 있음.

sum_a=get_all_sum(A_list) # a에서
sum_b=get_all_sum(B_list)

counterB=Counter(sum_b)
answer=0

for a in sum_a:
    answer+=counterB[T-a]


print(answer)