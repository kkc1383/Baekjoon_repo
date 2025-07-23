from collections import defaultdict
import sys

n=int(sys.stdin.readline().strip())
num_list=list(map(int,sys.stdin.readline().strip().split()))

num_dict=defaultdict(int)
for elem in num_list:
    num_dict[elem]+=1

qnum=int(sys.stdin.readline())
q_list=list(map(int,sys.stdin.readline().strip().split()))

answer=[]
for quest in q_list:
    if num_dict[quest]>0:
        answer.append(1)
    else:
        answer.append(0)

print(' '.join(map(str,answer)))