from itertools import permutations
import sys

n=int(sys.stdin.readline().strip())
cost=[[0]* n for _ in range(n)]
for i in range(n):
    cost[i]=list(map(int,sys.stdin.readline().strip().split()))

travel_list=list(range(1,n))
min_value=float('inf')
for p in permutations(travel_list):
    total=0
    valid=True
    p=[0]+list(p)+[0] # 양 끝에 출발도시 고정
    for i in range(len(p)-1):
        if cost[p[i]][p[i+1]]==0:
            valid=False
            break
        total+=cost[p[i]][p[i+1]]
    if valid:
        min_value=min(total,min_value)

print(min_value)