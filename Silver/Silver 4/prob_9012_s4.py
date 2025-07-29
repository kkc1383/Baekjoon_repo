import sys

n=int(sys.stdin.readline().strip())

for _ in range(n):
    input_value=list(sys.stdin.readline().rstrip())
    stack_list=[]
    illegal=False
    for elem in input_value:
        if elem=="(":
            stack_list.append(1)
        else:
            if len(stack_list)==0:
                illegal=True
                break
            stack_list.pop()
    if len(stack_list)!=0 or illegal:
        print("NO")
    else:
        print("YES")
