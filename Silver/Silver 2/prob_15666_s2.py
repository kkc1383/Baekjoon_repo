from itertools import combinations, combinations_with_replacement
import sys

n,m=list(map(int,sys.stdin.readline().strip().split()))

my_set=set(map(int,sys.stdin.readline().strip().split()))
my_list=list(my_set)
my_list.sort()

result_list=[]
for p in combinations_with_replacement(my_list,m):
    result_list.append(p)

result_list.sort()

for elem in result_list:
    print(*elem,sep=" ")