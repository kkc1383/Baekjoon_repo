import sys

house_num=int(sys.stdin.readline().strip())

color_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(house_num)]

dp_red=[[float("inf")]*3 for _ in range(house_num)] # 0이 빨강, 1이 초록, 2가 파랑
dp_green=[[float("inf")]*3 for _ in range(house_num)] # 0이 빨강, 1이 초록, 2가 파랑
dp_blue=[[float("inf")]*3 for _ in range(house_num)] # 0이 빨강, 1이 초록, 2가 파랑

dp_red[0][0]=color_list[0][0]
dp_green[0][1]=color_list[0][1]
dp_blue[0][2]=color_list[0][2]

# color_list.append([color_list[0][0],color_list[0][1],color_list[0][2]])

for i in range(1,house_num): # 첫 집을 빨간색으로 칠했을 경우, 마지막집은 빨간색이 될 수 없다. 
    if i==1:
        dp_red[i][1]=dp_red[i-1][0]+color_list[i][1]
        dp_red[i][2]=dp_red[i-1][0]+color_list[i][2]
    elif i==house_num-1:
        dp_red[i][1]=min(dp_red[i-1][0],dp_red[i-1][2])+color_list[i][1]
        dp_red[i][2]=min(dp_red[i-1][0],dp_red[i-1][1])+color_list[i][2]
    else:
        dp_red[i][0]=min(dp_red[i-1][1],dp_red[i-1][2])+color_list[i][0]
        dp_red[i][1]=min(dp_red[i-1][0],dp_red[i-1][2])+color_list[i][1]
        dp_red[i][2]=min(dp_red[i-1][0],dp_red[i-1][1])+color_list[i][2]
    
for i in range(1,house_num): # 첫 집을 초록색으로 칠했을 경우, 마지막집은 초록색이 될 수 없다. 
    if i==1:
        dp_green[i][0]=dp_green[i-1][1]+color_list[i][0]
        dp_green[i][2]=dp_green[i-1][1]+color_list[i][2]
    elif i==house_num-1:
        dp_green[i][0]=min(dp_green[i-1][1],dp_green[i-1][2])+color_list[i][0]
        dp_green[i][2]=min(dp_green[i-1][0],dp_green[i-1][1])+color_list[i][2]
    else:
        dp_green[i][0]=min(dp_green[i-1][1],dp_green[i-1][2])+color_list[i][0]
        dp_green[i][1]=min(dp_green[i-1][0],dp_green[i-1][2])+color_list[i][1]
        dp_green[i][2]=min(dp_green[i-1][0],dp_green[i-1][1])+color_list[i][2]

for i in range(1,house_num): # 첫 집을 파란색으로 칠했을 경우, 마지막집은 파란색이 될 수 없다. 
    if i==1:
        dp_blue[i][1]=dp_blue[i-1][2]+color_list[i][1]
        dp_blue[i][0]=dp_blue[i-1][2]+color_list[i][0]
    elif i==house_num-1:
        dp_blue[i][1]=min(dp_blue[i-1][0],dp_blue[i-1][2])+color_list[i][1]
        dp_blue[i][0]=min(dp_blue[i-1][2],dp_blue[i-1][1])+color_list[i][0]
    else:
        dp_blue[i][0]=min(dp_blue[i-1][1],dp_blue[i-1][2])+color_list[i][0]
        dp_blue[i][1]=min(dp_blue[i-1][0],dp_blue[i-1][2])+color_list[i][1]
        dp_blue[i][2]=min(dp_blue[i-1][0],dp_blue[i-1][1])+color_list[i][2]

total=dp_red[house_num-1]+dp_blue[house_num-1]+dp_green[house_num-1]
print(min(total))


# 각 색깔별로 dp 테이블을 따로만들어서 각 경우의 수에서 최솟값을 받기