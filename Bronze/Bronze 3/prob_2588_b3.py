import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
b_list=list(map(int,str(b)))
for i in reversed(b_list):
    print(a*i)
print(a*b)