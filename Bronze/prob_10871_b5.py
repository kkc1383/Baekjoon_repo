import sys

n,x=list(map(int,sys.stdin.readline().strip().split(' ')))
input_list=list(map(int,sys.stdin.readline().strip().split(' ')))
for i in input_list:
    if i < x:
        print(i, end=' ')