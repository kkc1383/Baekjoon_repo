import bisect
import sys

num=int(sys.stdin.readline().strip())

line_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(num)]

line_list.sort(key=lambda x : x[0])

num_list=[]
for start,end in line_list:
    num_list.append(end)


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

print(num-len(stack))