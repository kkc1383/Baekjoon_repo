import sys

total_ver, total_hor=list(map(int,sys.stdin.readline().strip().split())) # 총 가로길이, 총 세로길이
n=int(sys.stdin.readline().strip())
ver_list=[]
hor_list=[]
for _ in range(n):
    input_value=list(map(int,sys.stdin.readline().strip().split()))
    if(input_value[0]==0): # 가로 자르기
        ver_list.append(input_value[1])
    else:
        hor_list.append(input_value[1])

ver_list.sort()
hor_list.sort()
new_ver_list=[] # a1, a2-a1, hor-a2
new_hor_list=[] # b1, b2-b1, vet-b2
last_elem=0
for i in range(len(ver_list)):
    if i==0:
        new_ver_list.append(ver_list[i])
    else:
        new_ver_list.append(ver_list[i]-ver_list[i-1])
    last_elem=ver_list[i]
new_ver_list.append(total_hor-last_elem)

for i in range(len(hor_list)):
    if i==0:
        new_hor_list.append(hor_list[i])
    else:
        new_hor_list.append(hor_list[i]-hor_list[i-1])
    last_elem=hor_list[i]
new_hor_list.append(total_ver-last_elem)

width_list=[]
for i in new_ver_list:
    for j in new_hor_list:
        width_list.append(i*j)
        
print(max(width_list))