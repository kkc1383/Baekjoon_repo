import sys

n=int(sys.stdin.readline().rstrip())
num_list=list(map(int,sys.stdin.readline().rstrip().split()))

num_list.sort(reverse=True)
result=0
for i in range(len(num_list)):
    result+=sum(num_list[i:])

print(result)