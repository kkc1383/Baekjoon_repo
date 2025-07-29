import sys

n=int(sys.stdin.readline().rstrip())
num_list=list(map(int,sys.stdin.readline().rstrip().split()))
count_dict={}
for elem in num_list:
    try:
        count_dict[elem]+=1
    except KeyError:
        count_dict[elem]=1


n=int(sys.stdin.readline().rstrip())
check_list=list(map(int,sys.stdin.readline().rstrip().split()))

for elem in check_list:
    try:
        print(count_dict[elem], end=" ")
    except KeyError:
        print(0, end=" ")