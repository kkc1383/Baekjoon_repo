from collections import deque
import sys

n=int(sys.stdin.readline().strip())

myqueue=deque()
for _ in range(n):
    command=list(sys.stdin.readline().rstrip().split())
    if command[0]=="push":
        myqueue.append(int(command[1]))
    if command[0]=="pop":
        if len(myqueue)==0:
            print(-1)
        else:
            print(myqueue.popleft())
    if command[0]=="size":
        print(len(myqueue))
    if command[0]=="empty":
        if len(myqueue)==0:
            print(1)
        else:
            print(0)
    if command[0]=="front":
        if len(myqueue)==0:
            print(-1)
        else:
            print(myqueue[0])
    if command[0]=="back":
        if len(myqueue)==0:
            print(-1)
        else:
            print(myqueue[-1])