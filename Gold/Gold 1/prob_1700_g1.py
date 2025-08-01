from collections import deque
import sys

plug_num,use_num=list(map(int,sys.stdin.readline().strip().split()))

use_list=list(map(int,sys.stdin.readline().strip().split()))    

choose_list=[deque() for _ in range(use_num+1)]

have_set=set()
for i,elec in enumerate(use_list):
    choose_list[elec].append(i)
    have_set.add(elec)

plug_set=set()
plug_count=0
popoff_count=0
for i,elec in enumerate(use_list):
    if elec in plug_set: # 이미 꽂혀 있다면
        choose_list[elec].popleft()
        continue
    if plug_count<plug_num: # 더 꽂아도 될때
        choose_list[elec].popleft() # deque에서 빼주고
        plug_count+=1 # 플러그 꽂은만큼 더해주고
        plug_set.add(elec) # 플러그 셋에 올렺고
    else: # 이제부터 플러그를 뽑아야함
        # 뽑아야 하는데 뭘 뽑을지를 생각해야함
        popoff_count+=1
        max_elec=0
        max_index=0
        for plug_in in plug_set: #플러그에 꽂혀 있는 애들 중에
            if len(choose_list[plug_in])==0: # 앞으로 뽑을게 없거나
                max_elec=plug_in
                max_index=float('inf')
                break
            else: # 가장 큰 멀리 있는 가전제품을 찾는다.
                if max_index<choose_list[plug_in][0]:
                    max_index=choose_list[plug_in][0]
                    max_elec=plug_in
        plug_set.discard(max_elec)
        plug_set.add(elec)
        choose_list[elec].popleft()
print(popoff_count)