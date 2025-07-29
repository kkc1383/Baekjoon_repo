import sys

n=int(sys.stdin.readline().rstrip())
color_map=[]
for _ in range(n):
    input_value=list(map(int,sys.stdin.readline().rstrip().split()))
    color_map.append(input_value)

def isOne(x,y,level):
    white_count=0
    blue_count=0
    for i in range(1<<level): # 2^level
        for j in range(1<<level):
            if color_map[y+i][x+j] == 0 : # 흰 색
                white_count+=1
            else:   # 파란색
                blue_count+=1
    return (white_count!=0)+(blue_count!=0)==1

def cut_map(x,y,level):
    white_blue=[0,0]
    dx=(0,1<<(level-1),0,1<<(level-1))  # 2^(level-1)
    dy=(0,0,1<<(level-1),1<<(level-1))
    if level==1:
        if color_map[y][x]==0 and color_map[y][x+1]==0 and color_map[y+1][x]==0 and color_map[y+1][x+1]==0: # 싹다 흰색이면
            white_blue[0]+=1
        elif color_map[y][x]==1 and color_map[y][x+1]==1 and color_map[y+1][x]==1 and color_map[y+1][x+1]==1: # 싹다 파란색이면
            white_blue[1]+=1
        else:
            for i in range(4):  
                if color_map[y+dy[i]][x+dx[i]]==0:
                    white_blue[0]+=1
                else:
                    white_blue[1]+=1
    else:
        if isOne(x,y,level):
            if color_map[y][x]==0:
                white_blue[0]+=1
            else:
                white_blue[1]+=1
        else:
            for i in range(4):    
                if isOne(x+dx[i],y+dy[i],level-1): # 하위 사분면이 통일 된 것이면
                    if color_map[y+dy[i]][x+dx[i]]==0:  # 흰색일때
                        white_blue[0]+=1
                    else:   #  파란색일때
                        white_blue[1]+=1

                else:
                    temp=cut_map(x+dx[i],y+dy[i],level-1)
                    white_blue[0]+=temp[0]
                    white_blue[1]+=temp[1]
    return white_blue

answer=cut_map(0,0,n.bit_length()-1)#
print(answer[0]) # white
print(answer[1]) # blue

# 처음에는 isOne 함수 return 구분쪽 논리 처리가 잘못되었음
# 그 이후로는 계속 애초에 전체가 단색일때 level=1일때나 level=2일때나 모두 처리가 안되어 있어서 틀렸었던 것임