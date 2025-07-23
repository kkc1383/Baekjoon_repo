import heapq
import sys

n=int(sys.stdin.readline().strip())

min_heap=[]
for i in range(n):
    input_value=int(sys.stdin.readline().strip())
    if input_value==0:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap,input_value)

# 최솟값을 O(log n)으로 정렬해주는 힙 반드시 알아야 겠죠?
# 대신에 상단에서부터 뽑아쓰는경우밖에 못씁니다. 인덱스로 접근하기가 굉장히 어려움