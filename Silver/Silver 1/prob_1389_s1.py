from collections import defaultdict, deque
import sys

friend_num,edge_num=list(map(int,sys.stdin.readline().strip().split()))

edge_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(edge_num)]

INF=float('inf')
adj_list=[[INF]*(friend_num+1) for _ in range(friend_num+1)] # adj_list[i][j]는 i에서 j까지 가는데 거리

for s,e in edge_list:
    adj_list[s][e]=1
    adj_list[e][s]=1

for k in range(1,friend_num+1):
    for y in range(1,friend_num+1):
        for x in range(1,friend_num+1):
            if y==x:
                adj_list[y][x]=0
            else:
                adj_list[y][x]=min(adj_list[y][x],adj_list[y][k]+adj_list[k][x])

count=[INF]*(friend_num+1)

for i in range(1,friend_num+1):
    count[i]=sum(adj_list[i][1:])

min_count=min(count)
for i in range(1,friend_num+1):
    if count[i]==min_count:
        print(i)
        break

# 모든 정점에 대해서 모든 정점으로 다 가야하는 문제는 플로이드 워셜을 쓰자
# 괜히 bfs쓰려고했다가 거리 수 정하는게 난감해졌음 원래 degree로 1씩 올려가면 서하려고 했는데 알듯이 큐의 경계를 정하기가 매우 빡셈