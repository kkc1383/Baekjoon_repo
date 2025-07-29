import sys

n=int(sys.stdin.readline().strip())
stack_list=[]
for _ in range(n):
    command=sys.stdin.readline().rstrip().split()
    if command[0]=="push":
        stack_list.append(int(command[1]))
    elif command[0]=="pop":
        if len(stack_list)==0:
            print(-1)
        else:
            poped=stack_list.pop()
            print(poped)
    elif command[0]=="size":
        print(len(stack_list))
    elif command[0]=="empty":
        if len(stack_list)==0:
            print(1)
        else:
            print(0)
    elif command[0]=="top":
        if len(stack_list)==0:
            print(-1)
        else:
            print(stack_list[-1])