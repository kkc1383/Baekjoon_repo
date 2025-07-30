from collections import deque
import sys

start,target=list(map(int,sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10**6)

def dfs(num):
    stack=[(num,0)]
    result=0
    while stack:
        top,top_count=stack.pop()
        if top==target:
            result=top_count
            break
        if top*2<=target:
            stack.append((top*2,top_count+1))
        if top*10+1<=target:
            stack.append((top*10+1,top_count+1))

    return result

answer=dfs(start)
if answer==0:
    print(-1)
else:
    print(answer+1)

# 수가 작아질수가 없기 때문에 이전 것을 답습할 필요가 전혀 없다.
# 메모리초과나서 그냥 dfs로 풀었음
