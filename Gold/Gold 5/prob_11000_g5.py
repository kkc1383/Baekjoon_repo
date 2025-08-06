import heapq
import sys

num=int(sys.stdin.readline().strip())

lecture_list=[tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(num)]

lecture_list.sort(key=lambda x: (x[0],x[1]))

count=0
min_heap=[]
for start,end in lecture_list:
    if not min_heap:
        count+=1
        heapq.heappush(min_heap,end)
    else:
        if start<min_heap[0]:
            count+=1
            heapq.heappush(min_heap,end)
        else:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap,end)

print(count)

# 이 문제는 일단 시작지점순으로 오름차순을 해서 시작을 했다면 끝나는시간을 우선순위큐에 넣습니다.
# 그리고 그다음 강의 시작시간이 우선순위큐의 루트와 비교해서 빠르다면, 강의실을 추가합니다.
# 혹여 우선순위큐의 루트와 같거나 크다면 그 강의는 끝난거기 때문에 그냥 강의실 별도 추가없이 그 강의를 시작(우선순위큐에 삽입)하면 됩니다.