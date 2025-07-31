from collections import defaultdict
import sys

n=int(sys.stdin.readline().strip())
num_list=list(map(int,sys.stdin.readline().strip().split()))
answer_num=int(sys.stdin.readline().strip())
answer_list=list(map(int,sys.stdin.readline().strip().split()))

num_dict=defaultdict(int) # dict 초기화

for num in num_list: # key : 배열의 숫자, value= 배열의 숫자가 나온 횟수
    num_dict[num]+=1

result_list=[] # 해답을 저장하기 위한 공간
for answer in answer_list:
    if num_dict[answer]>0: # 원래 배열에 그 숫자가 있다면 0보다 클 것이기 때문에
        result_list.append(1)
    else: # 원래 배열에 그 숫자가 없다면
        result_list.append(0)

print(*result_list,sep=" ") # list의 [ ] 를 떼고 각 원소를 스페이스 한칸으로 구분하는 출력방법입니다.

# 배열을 하고 이분탐색을 통해서 푸는 방법도 있다고 생각하지만, 배열의 크기가 커질수록 시간이 길어지기에 O(n)으로 끝낼 수 있는 해시테이블로 해결했습니다.
# 