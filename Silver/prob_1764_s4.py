import sys


hear,see=list(map(int,sys.stdin.readline().rstrip().split()))
hear_dict={}
hear_see_list=[]
hear_see_count=0
for _ in range(hear):
    input_value=sys.stdin.readline().rstrip()
    hear_dict[input_value]=1

for _ in range(see):
    input_value=sys.stdin.readline().rstrip()
    if input_value in hear_dict.keys():
        hear_see_list.append(input_value)

hear_see_list.sort()
print(len(hear_see_list))
for elem in hear_see_list:
    print(elem)


