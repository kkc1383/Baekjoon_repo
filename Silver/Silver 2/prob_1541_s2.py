import re
import sys

input_value=sys.stdin.readline().rstrip()
my_list=re.findall(r'\d+|[+-]',input_value)
for i in range(len(my_list)):
    my_list[i]=my_list[i].lstrip('0')

sum=0
isMinus=False
for i in range(len(my_list)):
    if my_list[i]=='-':
        isMinus=True
    elif my_list[i]!='+':
        if isMinus:
            sum-=int(my_list[i])
        else:
            sum+=int(my_list[i])
print(sum)