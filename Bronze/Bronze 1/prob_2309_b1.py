import sys

height_list=[]

for _ in range(9):
    height_list.append(int(sys.stdin.readline().strip()))

height_list=sorted(height_list, reverse=True)
for elem in height_list:
    over_100=sum(height_list)-100
    if (over_100-elem) in height_list:
        height_list.remove(elem)
        height_list.remove(over_100-elem)
        
height_list.sort()
for elem in height_list:
    print(elem)