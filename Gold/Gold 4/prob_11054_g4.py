import bisect
from collections import deque
import sys

num=int(sys.stdin.readline().strip())

num_list=list(map(int,sys.stdin.readline().strip().split()))

inc=[0]*(num)
dec=[0]*(num)

# i번째 수까지 올라가는 수열 구하기
for i in range(num):
    inc_stack=[]
    for j in range(i): # 자기 자신은 이미 맨마지막에 담았다고 생각하고
        comp=num_list[j]
        if num_list[i]> comp: # 일단 무조건 i번째 원소보다 작아야하고
            if not inc_stack:
                inc_stack.append(comp)
            else:
                if comp>inc_stack[-1]:
                    inc_stack.append(comp)
                else:
                    index=bisect.bisect_left(inc_stack,comp)
                    inc_stack[index]=comp
    inc[i]=len(inc_stack)

num_list.reverse() # num_list 반전 (요게 포인트)

# i번째 수까지 내려가는 수 구하기 (인데 반전해서 똑같이 올라가는 수 구하기)
for i in range(num):
    dec_stack=[]
    for j in range(i): # 자기 자신은 이미 맨마지막에 담았다고 생각하고
        comp=num_list[j]
        if num_list[i]> comp: # 일단 무조건 i번째 원소보다 작아야하고
            if not dec_stack:
                dec_stack.append(comp)
            else:
                if comp>dec_stack[-1]:
                    
                    dec_stack.append(comp)
                else:
                    index=bisect.bisect_left(dec_stack,comp)
                    dec_stack[index]=comp
    dec[num-i-1]+=len(dec_stack)


length_list=[0]*(num)

for n in range(num):
    length_list[n]=inc[n]+dec[n]+1 # 여기서 1은 자기자신

print(max(length_list))

# 바이토닉은 그냥 n^2 걸리더라도 그냥 하는게 나을듯 한 숫자 짚고 왼쪽부터 스택 쌓고 오른쪽으로 내려가면서 최댓값 적어두기
# 사실 내가하는 방향이 맞았다
# i번째 까지 올라가는 수열 bisect로 구하고 O(nlogn) 내려가는 수열 bisect로 구하고 O(nlogn) 이거 길이 비교하면 O(nlogn)으로 끝납니다.
# 그리고 i번째 수를 넣을지 말지는 본인 선택인데 저는 빼고 구해서 마지막에 본인수 포함해서 +1 해서 마무리했습니다.