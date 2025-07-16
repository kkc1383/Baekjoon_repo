import sys

n,m=list(map(int,sys.stdin.readline().rstrip().split()))
my_dict={}
for _ in range(n):
    input_value=sys.stdin.readline().rstrip().split()
    my_dict[input_value[0]]=input_value[1]

for _ in range(m):
    problem=sys.stdin.readline().rstrip()
    print(my_dict[problem])