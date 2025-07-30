from collections import deque
import heapq
import sys

start,end=list(map(int,sys.stdin.readline().strip().split()))

min_heap=[]
heapq.heappush(min_heap,(0,start))
dist=[-1]*(200001)
dist[start]=0
while min_heap:
    top_count,top=heapq.heappop(min_heap)

    if top==end:
        print(top_count)
        break

    if top<end and dist[top*2]==-1:
        dist[top*2]=top_count
        heapq.heappush(min_heap,(top_count,top*2))
        
    next_add=top+1
    if next_add<=end and dist[next_add]==-1:
        dist[next_add]=top_count+1
        heapq.heappush(min_heap,(top_count+1,next_add))


    next_sub=top-1
    if next_sub>=0 and dist[next_sub]==-1:
        dist[next_sub]=top_count+1
        heapq.heappush(min_heap,(top_count+1,next_sub))
    
    
# 0초후에 2*x로 움직인다는 것은 언제 대입해도 상관 없다는 것
# 현재 위치와 end 위치의 차를 이용해야할듯
# 1부터시작할때 x2가 +1때문에 중복제거되어서 없어지는것을 고쳤음
# 그냥 곱하기를 먼저 시켜줬음
# 생각해보면 +1보다 x2가 먼저하는게 무조건 이득이기때문에(코스트가 없으니까)
# 그리고 코스트가 작은거부터 빼서 하는게 이득이니까 힙큐를 씀 아픙로도 이런 문제 나올 확률 높음

