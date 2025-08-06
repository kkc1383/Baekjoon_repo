import bisect
import sys

num=int(sys.stdin.readline().strip())

num_list=list(map(int,sys.stdin.readline().strip().split()))

num_list.reverse()

stack=[]

for elem in num_list:
    if not stack:
        stack.append(elem)
    else:
        if stack[-1]<elem:
            stack.append(elem)
        else:
            index=bisect.bisect_left(stack,elem)
            stack[index]=elem

print(len(stack))

# 길이를 구할 때도 bisect로 집어 넣는거 매우 중요함 그래야지 벽이 허물어진다. 큰 수가 떡하니 막고 있으면 그다음 수들이 전혀 못들어감