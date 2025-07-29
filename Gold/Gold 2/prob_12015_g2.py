import bisect
import sys

n=int(sys.stdin.readline().strip())
num_list=list(map(int,sys.stdin.readline().strip().split()))

length_list=[]
for num in num_list:
    if not length_list:
        length_list.append(num)
    else:
        if length_list[-1]<num: # 뒤에 그냥 붙이면 됨
            length_list.append(num)
        else:
            index=bisect.bisect_left(length_list,num)
            length_list[index]=num
print(len(length_list))

# 최댓값이 맨 끝으로 나오게끔
# 이전 문제랑 똑같이 풀면 됨
