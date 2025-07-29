from collections import defaultdict
import sys

n=int(sys.stdin.readline().rstrip())
num_dict=defaultdict(int)
num_list=list(map(int,sys.stdin.readline().rstrip().split()))
for num in num_list:
    num_dict[num]=1

answer_num=int(sys.stdin.readline().rstrip())
answer_list=list(map(int,sys.stdin.readline().rstrip().split()))
for num in answer_list:
    if num_dict[num]==1:
        print(1)
    else:
        print(0)