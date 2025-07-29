import sys

n=int(sys.stdin.readline().strip())
stack_list=[]
for _ in range(n):
    input_value=int(sys.stdin.readline().strip())
    if len(stack_list)==0:
        stack_list.append(input_value)
    else:
        if input_value>=stack_list[-1]:
            while len(stack_list)!=0 and input_value>=stack_list[-1]:
                stack_list.pop()
            stack_list.append(input_value)
        else:
            stack_list.append(input_value)
print(len(stack_list))