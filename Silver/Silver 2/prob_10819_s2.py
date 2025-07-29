from itertools import permutations
import sys

n=int(sys.stdin.readline().strip())
number_list=list(map(int,sys.stdin.readline().strip().split()))
number_list.sort()

max_val=0

for p in permutations(number_list):
    total=0
    for i in range(1,n):
        total+=abs(p[i]-p[i-1])
    max_val=max(max_val,total)

print(max_val)