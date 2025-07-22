import heapq
import sys

n=int(sys.stdin.readline())
myqueue=[]
for _ in range(n):
    input_value=int(sys.stdin.readline())
    if input_value==0:
        if len(myqueue)==0:
            print(0)
        else:
            print(-heapq.heappop(myqueue))
    else:
        heapq.heappush(myqueue,-input_value)

# 힙큐 쓰는 방법 익히기
# heapq.메소드(쓰고싶은 배열)
# heapq는 리스트를 기본적으로 활용함
# 기존의 리스트를 힙 화시키고 싶으면 heapq.heapify(배열)