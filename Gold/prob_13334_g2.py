import bisect
import heapq
import sys

n=int(sys.stdin.readline().rstrip())
line_list=[sorted(list(map(int,sys.stdin.readline().strip().split()))) for _ in range(n)]
max_line=int(sys.stdin.readline().strip())

line_list.sort(key=lambda x:x[1]) # 오른쪽 x좌표 순으로 정렬 끝나는게 가장 왼쪽인 것부터
min_heap=[]
max_count=0

for start,end in line_list:
    if end-start >max_line: #어짜피 안되는 것들은 패스
        continue
    heapq.heappush(min_heap,start) # 오른쪽 x좌표순으로 정렬 했으니 heap에는 시작점이 작은게 앞으로 오게

    while min_heap and min_heap[0] < end-max_line: # end- max_line보다는 크거나 같아야 조건에 만족하는데 start중 가장 최소값부터 비교하면서 그 조건에 부합하는 start가 나올때까지 뽑아냄
        heapq.heappop(min_heap)
    max_count=max(max_count, len(min_heap))

print(max_count)
# people_queue=[]
# possible_queue=[]
# line_list.sort(key=lambda x:(x[0],x[1]))
# index=0
# max_coord=max([max(line) for line in line_list])
# while index<n:
#     line_start=line_list[index][0] # 철로의 시작 x 좌표
#     line_end=line_start+max_line   # 철로의 끝 x 좌표
#     new_index=index
#     while new_index<n:
#         if line_list[new_index][0]>=line_end: # 왼쪽 좌표가 철도 끝보다 크거나 같을 때
#             break
#         else:
#             heapq.heappush(possible_queue,line_list[new_index][1]) # 오른쪽 x좌표를 최소heap에 넣음
#         new_index+=1

#     count=0
#     while len(possible_queue)!=0: # possible queue안에 들어간 오른쪽 x좌표들을 오름차순으로 꺼내는데 철로의 범위를 벗어나면 바로 break
#         top=heapq.heappop(possible_queue)
#         if top>line_end:
#             break
#         count+=1
#     heapq.heappush(people_queue,-count)
#     if line_end>=max_coord: # 철도의 끝이 가장 큰 오른쪽 x좌표보다 크거나 같으면 더이상 탐색을 안해도 되니까 break
#         break
#     index+=1
# print(-heapq.heappop(people_queue))

# .sort() 함수는 리턴이 None임! 리턴이 필요할땐 sorted() 쓰기
# del line_list[0]은 O(n^2)의 시간복잡도를 가짐. 한칸씩 밀어야되서