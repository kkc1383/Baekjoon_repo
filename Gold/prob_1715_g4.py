import heapq
import sys

n=int(sys.stdin.readline())
card_list=[int(sys.stdin.readline().strip()) for _ in range(n)]

heapq.heapify(card_list)

if n==1:
    print(0)
else:
    heapq.heapify(card_list)
    total_cost=0
    while len(card_list)>1:
        a=heapq.heappop(card_list)
        b=heapq.heappop(card_list)
        cost=a+b
        total_cost+=cost
        heapq.heappush(card_list,cost)
    print(total_cost)

# 더한 값을 다시 heap에 넣는 방법, 그렇게 또 더할 수 있음.
# 그리고 작은 값끼리 더해야 하기 때문에, heapq에서 빼오면 됨