from itertools import combinations, permutations
import sys

n,m=list(map(int,sys.stdin.readline().strip().split()))

my_list=list(range(1,n+1))

for p in combinations(my_list,m):
    print(*list(p))