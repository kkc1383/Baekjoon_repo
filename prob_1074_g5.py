import sys

my_list=[]

def func(x,y,n):
    number=0
    if n==1:
        if x==0 and y==0:
            return 0
        elif x==1 and y==0:
            return 1
        elif x==0 and y==1:
            return 2
        elif x==1 and y==1:
            return 3
        else:
            return 0
    else:
        if 0<=x<(1<<(n-1)) and 0<=y<(1<<(n-1)): # 왼쪽 위
            number+=func(x,y,n-1)
        elif (1<<(n-1))<=x<(1<<n) and 0<=y<(1<<(n-1)): # 오른쪽 위
            number+=(1<<(2*n-2))
            number+=func(x-(1<<(n-1)),y,n-1)
        elif 0<=x<(1<<(n-1)) and (1<<(n-1))<=y<(1<<n): # 왼쪽 아래
            number+=(1<<(2*n-2))*2
            number+=func(x,y-(1<<(n-1)),n-1)
        elif (1<<(n-1))<=x<(1<<n) and (1<<(n-1))<=y<(1<<n): # 오른쪽 아래
            number+=(1<<(2*n-2))*3
            number+=func(x-(1<<(n-1)),y-(1<<(n-1)),n-1)
        else:
            return 0
            
        return number


N,r,c=list(map(int,sys.stdin.readline().strip().split()))
print(func(c,r,N))
