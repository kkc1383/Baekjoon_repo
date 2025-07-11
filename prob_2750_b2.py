import sys

n=int(sys.stdin.readline().strip())
my_list=[]
for _ in range(n):
    my_list.append(int(sys.stdin.readline().strip()))

my_list.sort()
for i in my_list:
    print(i)