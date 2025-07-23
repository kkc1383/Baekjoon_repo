import heapq
import sys

n=int(sys.stdin.readline().strip())

pos_list=[]
neg_list=[]
for _ in range(n):
    input_value=int(sys.stdin.readline().strip())
    if input_value==0:
        if not pos_list and not neg_list:
            print(0)
        elif not pos_list and neg_list: # 음수 힙에만 있을 경우
            print(-heapq.heappop(neg_list))
        elif pos_list and not neg_list: # 양수 힙에만 있을 경우
            print(heapq.heappop(pos_list))
        else:
            if neg_list[0]<=pos_list[0]: # 절댓값이 음수 힙 쪽이 작거나 같을 때 절댓값이 같다면 작은 값은 음수기 때문에 등호는 여기에 붙임
                print(-heapq.heappop(neg_list))
            else:
                print(heapq.heappop(pos_list))
    else:
        if input_value>0:
            heapq.heappush(pos_list,input_value)
        else:
            heapq.heappush(neg_list,-input_value)

# 음수 힙에 넣을땐 절댓값으로 넣었으니 비교할땐 - 안붙여도 된다. 아예 heappop할때만 붙이면 됨