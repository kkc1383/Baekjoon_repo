import heapq
import sys

n=int(sys.stdin.readline())
max_heap=[]
min_heap=[]
for i in range(n):
    input_value=int(sys.stdin.readline())
    heapq.heappush(max_heap,-input_value) #일단 max heap에 넣는다
    heapq.heappush(min_heap,-heapq.heappop(max_heap)) # 그다음 maxheap의 최댓값을 minheap에 넣는다.
    if len(min_heap)>len(max_heap): # max와 min의 크기를 맞춰줍니다. max가 1 많거나 같게
        heapq.heappush(max_heap,-heapq.heappop(min_heap)) 
    
    if len(min_heap)==len(max_heap):
        print(min(-max_heap[0],min_heap[0]))
    else:
        print(-max_heap[0])
    


# 두개의 힙을 사용하여 중간값을 찾는다.
# 최소~중간 은 최대힙을 사용
# 중간~최대 는 최소힙을 사용
# 포인트는 일단 max부터 거쳤다가 나온 최댓값을 min에도 넣어서 양쪽을 다 넣어야지 중간값이 성립이 됩니다.
