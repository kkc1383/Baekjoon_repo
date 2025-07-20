import sys

n=int(sys.stdin.readline().strip())

circle_list=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

coord_stack=[] # ("L or R", x 좌표, 반지름)
done_stack=[] # (반지름, target_count)
area_count=1
for circle in circle_list:
    coord_stack.append(("L",circle[0]-circle[1],circle[1]))
    coord_stack.append(("R",circle[0]+circle[1],circle[1]))
coord_stack.sort(key=lambda x: (x[1],   # 1순위, x좌표를 보고 오름차순으로 정렬
                                0 if x[0]=="R" else 1,  # 2순위, R이 먼저 오게끔 
                                x[2] if x[0] =="R" else -x[2] # 3순위, R들은 반지름이 오림차순, L들은 반지름이 내름차순으로 정렬
                                ))

while len(coord_stack)!=0:
    coord_top=coord_stack.pop()
    if coord_top[0]=="R":  # R 일때 done에 넣기
        done_stack.append([coord_top[2],0])
    else:
        done_top=done_stack.pop()
        if done_top[1]>=done_top[0]: # 최고 치를 만족했으면
            area_count+=1
        area_count+=1

        if len(done_stack)!=0: # 해결해야 하는 원이 있으면
            done_stack[-1][1]+=done_top[0]

print(area_count)

# left_stack=[] # 원을 그렸을 때 x축과 만나는 지점 중 왼쪽 점의 x좌표와 그 원의 반지름을 저장 (x좌표,반지름)이 하나의 스택의 자료형임
# right_stack=[] # 원을 그렸을 때 x축과 접점 중 우측 점 (x좌표, 반지름)
# done_stack=[] # 해결해야 하는 원의 반지름과 여태까지의 결산한 값을 저장 (반지름,target_count)
# area_count=1 # 총 영역의 수
# for circle in circle_list:
#     left_stack.append((circle[0]-circle[1],circle[1]))
#     right_stack.append((circle[0]+circle[1],circle[1]))
# left_stack.sort(key=lambda x: (x[0],-x[1])) # 우선 x값이 작은 순서대로 정렬하되 같은 것이 있다면 반지름 값이 큰 것이 앞으로 오도록
# right_stack.sort(key=lambda x: ((x[0],x[1]))) # 우선 x값이 작은 순서대로 정렬하되 같은 것이 있다면 반지름 값이 작은 것이 앞으로 오도록


# while len(left_stack)!=0:
#     # 괄호의 시작, 해결해야 하는 퀘스트를 받는다
#     if len(right_stack)!=0:  # 해결 해야 하는 원이 있을 때
#         right_top=right_stack.pop()
#         done_stack.append([right_top[1],0])
#     # 해결의 시작
#     if len(right_stack)==0 or right_stack[-1][0]<=right_top[0]-(right_top[1]*2): # 지금 해결해야하는 원 안에 다른 원이 없다면 결산
#         left_stack.pop()
#         done_top=done_stack.pop()

#         if done_top[1]>=done_top[0]: # 최고 치를 만족했으면
#             area_count+=1
#         area_count+=1

#         if len(done_stack)!=0: # 해결해야 하는 원이 있으면
#             done_stack[-1][1]+=done_top[0]

# print(area_count)

# 튜플 말고 리스트로해서 값을 변화시켜줘야하나
# 뭐가 문제냐면 결산을 하고 나왔을 때 부모에 대한 결산이 안 되어 있음.
# left_stack의 경우 빠져나올때 건드리게 되는데 어떻게 써먹을 방법이 생각이 안남
# 그래서 그냥 하나의 스택으로 통합한 다음 어떻게 하면 스택을 잘 정렬할 수 있을까 생각을 해서 각 우선순위를 정해서 정렬
# 그 이후는 단순 R이면 스택에 넣고 L이면 스택 빠져나오면서 target_count 올려주고