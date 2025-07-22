from collections import deque
import sys

n,k=list(map(int,sys.stdin.readline().strip().split()))

num_list=[i for i in range(1,n+1)]
index=k-1
result_queue=deque()
while len(num_list)>0:
    index%=len(num_list)
    poped=num_list[index]
    result_queue.append(poped)
    del num_list[index]
    index+=k-1

result_queue=list(result_queue)
print("<",end="")
print(", ".join(map(str,result_queue)), end="")
print(">")