import sys

n,m=list(map(int,sys.stdin.readline().rstrip().split()))

num_list=list(map(int,sys.stdin.readline().rstrip().split()))

for _ in range(m):
    start,end=list(map(int,sys.stdin.readline().rstrip().split()))
    bit=0
    for i in range(end-start+1):
        bit+=(1<<i)
    bit=bit<<(start-1)  


    print(sum(num_list[start-1:end]))