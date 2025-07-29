import bisect
from collections import deque
import sys

n=int(sys.stdin.readline().strip())
num_list=list(map(int,sys.stdin.readline().strip().split()))

num_index=0
long_list=[]
for num in num_list:
    if not long_list:
        long_list.append([[num,num_index]])
        num_index+=1
    else:
        if long_list[-1][-1][0]<num:
            long_list.append([[num,num_index]])
            num_index+=1
        else:
            index=bisect.bisect_left(long_list,num, key=lambda x: x[-1][0])
            long_list[index]+=[[num,num_index]]
            num_index+=1
find_list=deque()
next_index=num_index
for line in reversed(long_list):
    if len(line)==1:
        next_index=line[0][1]
        find_list.appendleft(line[0][0])
    else:
        index=bisect.bisect_left(line,next_index,key=lambda x: x[1])
        if index==0:
            find_list.appendleft(line[0][0])
            next_index=line[0][1]
        else:
            find_list.appendleft(line[index-1][0])
            next_index=line[index-1][1]

print(len(long_list))
print(' '.join(map(str,find_list)))

# 감사합니다....
# index를 같이 저장해놓고 이분탐색으로 정해야하는 index를 찾아서 뒤에서부터 탐색
# 그니까 longlist에다가 원소를 날리지말고 계속 쌓아가는데 그 쌓는 자료형이 (숫자,몇번째) 이래서 총 3차원 list가 생기는 것이고
# 몇번째는 맨 뒤에서부터 봤을때 이어지는 수열인지 확인하기 위해서 인덱스가 내려가야 하기때문에 인덱스를 저장한 것이고
# 그렇다면 인덱스가 작아지는 범위 내에서 가장 큰 인덱스를 찾아야되서 이분탐색으로 찾은 것임

