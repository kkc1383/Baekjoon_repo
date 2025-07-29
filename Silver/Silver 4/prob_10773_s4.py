import sys

n=int(sys.stdin.readline().rstrip())
stack_list=[]
for _ in range(n):
    input_value=int(sys.stdin.readline().strip())
    if input_value==0:
        top=stack_list.pop()
    else:
        stack_list.append(input_value)
print(sum(stack_list))