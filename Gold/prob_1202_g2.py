import heapq
import sys

n,k=list(map(int,sys.stdin.readline().strip().split()))
jewel_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)] # (무게, 가격)
bag_list=[int(sys.stdin.readline().strip()) for _ in range(k)]

jewel_list.sort() # 보석을 작은것부터 담겠다.
bag_list.sort() # 가방을 작은것부터 담겠다.

max_heap=[]
index=0 # 아직 넣지 않은 보석의 인덱스
answer=0

for cap in bag_list:
    # 현재 가방에 들어갈 수 있는 보석 push.  넣을 수 있는 보석은 일단 다 힙에 넣고 보는거 그리고 가치 순으로 빼기
    while index<n and jewel_list[index][0]<=cap:
        weight,value=jewel_list[index]
        heapq.heappush(max_heap,-value)
        index+=1
    if max_heap:
        answer+=-heapq.heappop(max_heap)
print(answer)


# 힙큐를 쓰는 공식중에 하나가 일단 정렬을 작은것부터 해놓고 가능성이 있는 것들에 대해서 일단 힙큐에 넣은다음에 가치가 가장 큰것부터 빼옴
# 그렇게 되면 빠르게 가장 효율적인 선택지를 할 수 있음. just like 철도 문제
# 가방에 단 하나밖에 보석을 못 넣는 거였어 그래서 힙큐를 쓴 것이었고