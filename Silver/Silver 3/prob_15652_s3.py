from itertools import combinations, combinations_with_replacement
import sys

n,m=list(map(int,sys.stdin.readline().strip().split()))

my_list=list(range(1,n+1))


for p in combinations_with_replacement(my_list,m):
    print(*list(p))

# 중복 가능한 조합 combinations with replacement 개꿀