from collections import deque
import heapq
import sys

n,k=list(map(int,sys.stdin.readline().strip().split()))

coin_list=[int(sys.stdin.readline().strip()) for _ in range(n)]

INF=float('inf')
dist=[INF]*100001 # index원을 만들기 위해서 든 최소의 동전 갯수
myqueue=deque() # 동전갯수, 코스트
myqueue.append((0,0))
while myqueue:
    top=myqueue.popleft() 
    top_count=top[0]
    top_cost=top[1]
    for coin in coin_list: # 모든 동전들을 다 더해보기
        if top_cost+coin>k: # 이미 넘어버렸다면 패스
            continue
        if dist[top_cost+coin]>top_count+1: # 원래 기록된 것이 더 크다면
            dist[top_cost+coin]=top_count+1
            myqueue.append((top_count+1,top_cost+coin))
            

print(-1 if dist[k]==INF else dist[k])

# 하나씩 다해보는거지 bfs 느낌으로