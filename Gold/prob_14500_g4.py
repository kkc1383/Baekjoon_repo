import sys

n,m=list(map(int,sys.stdin.readline().rstrip().split()))
num_map=[]
for _ in range(n):
    input_value=list(map(int,sys.stdin.readline().rstrip().split()))
    num_map.append(input_value)

#square, I, L, S, T

def get_square(x,y):
    return num_map[y][x]+num_map[y][x+1]+num_map[y+1][x]+num_map[y+1][x+1]
def get_I_hor(x,y):
    return num_map[y][x]+num_map[y+1][x]+num_map[y+2][x]+num_map[y+3][x]
def get_I_ver(x,y):    
    return num_map[y][x]+num_map[y][x+1]+num_map[y][x+2]+num_map[y][x+3]
def get_L_1(x,y): 
    return num_map[y][x]+num_map[y][x+1]+num_map[y+1][x+1]+num_map[y+2][x+1]
def get_L_2(x,y): 
    return num_map[y][x]+num_map[y+1][x]+num_map[y+2][x]+num_map[y][x+1]
def get_L_3(x,y): 
    return num_map[y][x]+num_map[y+1][x]+num_map[y+2][x]+num_map[y+2][x+1]
def get_L_4(x,y): 
    return num_map[y+2][x]+num_map[y+2][x+1]+num_map[y+1][x+1]+num_map[y][x+1]
def get_L_5(x,y): 
    return num_map[y][x]+num_map[y][x+1]+num_map[y][x+2]+num_map[y+1][x]
def get_L_6(x,y): 
    return num_map[y][x]+num_map[y][x+1]+num_map[y][x+2]+num_map[y+1][x+2]
def get_L_7(x,y): 
    return num_map[y][x]+num_map[y+1][x]+num_map[y+1][x+1]+num_map[y+1][x+2]
def get_L_8(x,y): 
    return num_map[y+1][x]+num_map[y+1][x+1]+num_map[y+1][x+2]+num_map[y][x+2]
def get_S_1(x,y):
    return num_map[y][x]+num_map[y][x+1]+num_map[y+1][x+1]+num_map[y+1][x+2]
def get_S_2(x,y):
    return num_map[y+1][x]+num_map[y+1][x+1]+num_map[y][x+1]+num_map[y][x+2]
def get_S_3(x,y):
    return num_map[y+2][x]+num_map[y+1][x]+num_map[y+1][x+1]+num_map[y][x+1]
def get_S_4(x,y):
    return num_map[y][x]+num_map[y+1][x]+num_map[y+1][x+1]+num_map[y+2][x+1]
def get_T_1(x,y):
    return num_map[y][x]+num_map[y][x+1]+num_map[y][x+2]+num_map[y+1][x+1]
def get_T_2(x,y):
    return num_map[y+1][x]+num_map[y][x+1]+num_map[y+1][x+1]+num_map[y+1][x+2]
def get_T_3(x,y):
    return num_map[y][x]+num_map[y+1][x]+num_map[y+2][x]+num_map[y+1][x+1]
def get_T_4(x,y):
    return num_map[y+1][x]+num_map[y][x+1]+num_map[y+1][x+1]+num_map[y+2][x+1]

def find_max_square():
    max_value=0
    if n>=2 and m>=2: # 2*2보다 큰지
        for hor in range(n-2+1):
            for ver in range(m-2+1):
                max_value=max(max_value,get_square(ver,hor))
    return max_value
def find_max_I():
    max_value=0
    if n>=4 and m>=1: # 세로
        for hor in range(n-4+1):
            for ver in range(m-1+1):
                max_value=max(max_value,get_I_hor(ver,hor))
    if n>=1 and m>=4: # 가로
        for hor in range(n-1+1):
            for ver in range(m-4+1):
                max_value=max(max_value,get_I_ver(ver,hor))
    return max_value

def find_max_L():
    max_value=0
    if n>=3 and m>=2: # 세로로 길게 1~4번
        for hor in range(n-3+1):
            for ver in range(m-2+1):
                max_value=max(max_value,get_L_1(ver,hor))
                max_value=max(max_value,get_L_2(ver,hor))
                max_value=max(max_value,get_L_3(ver,hor))
                max_value=max(max_value,get_L_4(ver,hor))
    if n>=2 and m>=3: # 가로로 길게 5~8번
        for hor in range(n-2+1):
            for ver in range(m-3+1):
                max_value=max(max_value,get_L_5(ver,hor))
                max_value=max(max_value,get_L_6(ver,hor))
                max_value=max(max_value,get_L_7(ver,hor))
                max_value=max(max_value,get_L_8(ver,hor))
    return max_value

def find_max_S():
    max_value=0
    if n>=2 and m>=3: # 가로로 길게 1~2번
        for hor in range(n-2+1):
            for ver in range(m-3+1):
                max_value=max(max_value,get_S_1(ver,hor))
                max_value=max(max_value,get_S_2(ver,hor))
    if n>=3 and m>=2: # 세로로 길게 3~4번
        for hor in range(n-3+1):
            for ver in range(m-2+1):
                max_value=max(max_value,get_S_3(ver,hor))
                max_value=max(max_value,get_S_4(ver,hor))
    return max_value

def find_max_T():
    max_value=0
    if n>=2 and m>=3: # 가로로 길게 ㅜ 1~2번
        for hor in range(n-2+1):
            for ver in range(m-3+1):
                max_value=max(max_value,get_T_1(ver,hor))
                max_value=max(max_value,get_T_2(ver,hor))
    if n>=3 and m>=2: # 세로로 길게 ㅓ 3~4번
        for hor in range(n-3+1):
            for ver in range(m-2+1):
                max_value=max(max_value,get_T_3(ver,hor))
                max_value=max(max_value,get_T_4(ver,hor))
    return max_value


max_result=max(find_max_I(),find_max_L(),find_max_S(),find_max_square(),find_max_T())
print(max_result)