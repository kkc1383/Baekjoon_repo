from itertools import combinations, combinations_with_replacement, permutations
import sys

n,m=list(map(int,sys.stdin.readline().strip().split()))

my_list=list(map(int,sys.stdin.readline().strip().split()))

result_list=[]
for p in set(permutations(my_list,m)):
    result_list.append(p)

result_list.sort()

for line in result_list:
    print(*line)
