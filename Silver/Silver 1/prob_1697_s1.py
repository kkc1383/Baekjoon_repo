from collections import deque
import sys

start,end=list(map(int,sys.stdin.readline().strip().split()))


my_set=set()
my_set.add(start)
visited=[False]*(300000)
visited[start]=True
count=0
find=False
if start==end:
    print(0)
    sys.exit(0)
while my_set:
    extra=set()
    for elem in my_set:
        if elem*2==end or elem+1==end or elem-1==end:
            find=True
            break
        if not visited[elem*2] and elem*2<=100000:
            extra.add(elem*2)
            visited[elem*2]=True
        if not visited[elem+1] and elem+1<=100000:            
            extra.add(elem+1)
            visited[elem+1]=True
        if not visited[elem-1] and elem>0:
            extra.add(elem-1)
            visited[elem-1]=True
    my_set=extra
    count+=1
    if find:
        print(count)
        break

# 그냥 무식하게 했다. 끝이 10000이라 이에 넘지 않게 해주는게 중요하고, 처음과 끝이 같을 때 처리를 따로 해주는게 좋다.