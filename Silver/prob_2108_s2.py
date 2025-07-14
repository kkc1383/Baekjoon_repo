import sys

n=int(sys.stdin.readline().rstrip())
num_list=[]
for _ in range(n):
    input_value=int(sys.stdin.readline().rstrip())
    num_list.append(input_value)

    
num_list.sort()
print(round(sum(num_list)/len(num_list)))  # 산술평균

mid=len(num_list)//2
print(num_list[mid])  # 중앙값

# 최빈값
num_dict={}
for item in num_list:
    try:
        num_dict[item]+=1
    except KeyError:
        num_dict[item]=1

same_list=[]
max_value=-1
for key,value in num_dict.items():
    if max_value<value:
        max_value=value
        same_list=[]
        same_list.append(key)
    elif max_value==value:
        same_list.append(key)

if len(same_list)==1:
    print(same_list[0])
else:
    same_list.sort()
    print(same_list[1])


max_num=max(num_list)
min_num=min(num_list)
print(max_num-min_num) # 범위