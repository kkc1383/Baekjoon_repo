from bisect import bisect_left
import sys

sade_num,animal_num,shot_range=list(map(int,sys.stdin.readline().strip().split()))
sade_coord_list=list(map(int,sys.stdin.readline().strip().split()))
animal_coord_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(animal_num)]

sade_coord_list.sort()
count=0
for animal in animal_coord_list:
    if animal[1]>shot_range: # y좌표가 사정거리를 벗어나면 패스
        continue
    else:
        near_index=bisect_left(sade_coord_list,animal[0]) # 이러면 동물과 가장 가까운(하지만 동물보다 오른쪽에 있는) 사대의 index를 반환
        if 0<near_index<sade_num: # 사대들 사이에 동물이 있을 경우
            if abs(animal[0]-sade_coord_list[near_index])+animal[1] <=shot_range or abs(animal[0]-sade_coord_list[near_index-1])+animal[1] <=shot_range: # sade_coord_list[near_index-1]가 존재하고, 각 사대가 맨해튼 거리에 만족한다면
                count+=1
        else: # 사대들보다 왼쪽에 있거나 오른쪽에 있을 때
            if near_index==sade_num: #특히나 맨 오른쪽에 있을 때(어떠한 사대보다 동물의x좌표가 클때) near_index가 맨끝인덱스+1가 되어서 -1을 해서 indexerror를 방지
                near_index-=1
            if abs(animal[0]-sade_coord_list[near_index])+animal[1] <=shot_range:
                count+=1

print(count)
# 처음 착안은 정석대로 직선방정식을 이용해서 각 사대별로 동물들이 범위 안에 있으면 카운트 되게끔하였지만 숫자가 커지면 시간이 초과됨
# 따라서 동물을 기준으로 어짜피 y좌표가 shot_range를 초과해버리면 그냥 패스해버리고 x만 봤을 때 bisect_left를 사용하여 근처 2개 사대에 대해서만 거리 확인하고 둘중 하나라도 거리 안에 들어오면 체크
# 이러면 동물 수 n * 이진탐색 log m 으로 n log m 으로 구할 수 있다.


# count=0
# kill_set=set()
# for sade in sade_coord_list:
#     for animal in animal_coord_list:
#         if animal[1]-animal[0]<=shot_range-sade and animal[1]+animal[0]<=shot_range+sade:
#             if not (animal[0],animal[1]) in kill_set:
#                 count+=1
#                 kill_set.add((animal[0],animal[1]))
# print(count)
