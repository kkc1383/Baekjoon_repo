import sys

n = int(sys.stdin.readline())
for i in range(n):
    a,b = list(map(int,sys.stdin.readline().strip().split(' ')))
    print(a+b)