import sys

boardN=int(sys.stdin.readline().strip())
appleNum=int(sys.stdin.readline().strip())
apple_list=[]
for _ in range(appleNum):
    input_value=list(map(int,sys.stdin.readline().strip().split()))
    apple_list.append([input_value[1]-1,input_value[0]-1])
moveNum=int(sys.stdin.readline().strip())
direction_change_list=[list(sys.stdin.readline().strip().split()) for _ in range(moveNum)]

dx=[1,0,-1,0]  # 오른쪽 0, 아래 1, 왼쪽 2, 위 3
dy=[0,1,0,-1]

snake_coord=[[0,0,0]] # (x,y,걸린시간)
game_second=0 # 게임시간
direction=0 # 방향, 0,1,2,3 dx,dy의 index가 될거임
move_list=[[0,0]] # 각 초별 이동 dx,dy index초에 행동 양상이 value (dx,dy)
bonus_coord=[] # 사과를 먹었을 경우 맨마지막 좌표를 잠깐 가지고 있음.
isApple=False # 사과를 먹었을 경우 잠깐 true
isGameOver=False
while True:
    game_second+=1 # 게임시간 1초 증가 
    if len(direction_change_list)!=0 and game_second==int(direction_change_list[0][0])+1: # game_second초 후에 방향전환 지시가 있으면
        if direction_change_list[0][1]=="D": # R일때 rotation을 1증가시켜 시계방향으로 체인지
            direction=(direction+1)%4
        else: # L일때 rotation을 1빼서 반시계방향으로 체인지
            direction=(direction-1 if direction>0 else 3)
        del direction_change_list[0]

    # 행동양상을 각 초마다 저장
    move_list.append([dx[direction],dy[direction]])

    # 일단 머리부터 한칸 움직였다고 임시로 했을 때
    temp_head=[snake_coord[0][0]+move_list[snake_coord[0][2]+1][0],snake_coord[0][1]+move_list[snake_coord[0][2]+1][1]]
   
    # 뱀의 머리 위치로 게임 오버 상황 판단
    if temp_head[0]>=boardN or temp_head[0]<0 or temp_head[1]>=boardN or temp_head[1]<0: # 맵 밖을 벗어났을 경우
        break
    for snake in snake_coord[1:]: # 뱀의 머리가 다른 뱀의 부분과 맞닿은 경우
        if temp_head==snake[:-1]:
            isGameOver=True
            break
    if isGameOver:
        break

    # 뱀의 이동
    for snake in snake_coord:
        snake[2]+=1 # 각 뱀 부분당 걸린시간 1증가
        snake[0]+=move_list[snake[2]][0] # 걸린시간 별 행동 dx를 x에 더해줌
        snake[1]+=move_list[snake[2]][1] # 걸린시간 별 행동 dx를 y에 더해줌
    
    # 이전 행동에서 사과를 먹었을 경우 맨 마지막에 뱀의 부분 추가
    if isApple:
        snake_coord.append([bonus_coord[0],bonus_coord[1],snake_coord[-1][2]-1])
        isApple=False
        bonus_coord=[]

    
    if [snake_coord[0][0],snake_coord[0][1]] in apple_list: # 뱀의 머리에 사과가 있을 경우
        isApple=True
        bonus_coord=[snake_coord[-1][0],snake_coord[-1][1]] # 뱀의 맨 마지막 원소를 잠시 bonus_coord에 저장함
        apple_list.remove([snake_coord[0][0],snake_coord[0][1]])

print(game_second)
