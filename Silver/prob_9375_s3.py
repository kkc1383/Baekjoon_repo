from collections import defaultdict
from itertools import combinations
from math import prod
import sys

cases=int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n=int(sys.stdin.readline().rstrip())
    cloth_dict=defaultdict(int)
    for i in range(n):
        cloth,part=list(sys.stdin.readline().rstrip().split())
        cloth_dict[part]+=1
    
    plus1=[1]*len(cloth_dict)
    cloth_list=list(cloth_dict.values())
    cloth_list=[x+y for x,y in zip(plus1,cloth_list)]
    print(prod(cloth_list)-1)

    ## 이것도 수학적인 내용이었다. 조합을 이야기할때 오히려 벗어도 된다는 것은 해당 리스트에 0을 포함해서 돌린다는 것임
    # 이때 모두 다 벗는 것이 안되기 때문에 전부다 0인 케이스, 즉 1만 빼면 된다는 것임
    # 배웠던 적이 있다. 두 집합으로 만들 수 있는 모든 집합의 경우의 수는 각 원소+1끼리 곱하고 -1 해주는거임
    # 그리고 하나 알아갈 점은 리스트의 원소끼리 합 같은 경우 [x+y for x,y in zip(a,b)]이런식으로 표현한다.
    # dict.values()도 반환값이 dict.value 객체 이므로 list화 해주는 것도 중요