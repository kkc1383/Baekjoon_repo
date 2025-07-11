import sys
from typing import List

def put_queen(col_mask,cross1_mask, cross2_mask, row: int ,n : int): # flag는 bool list cross는 int list
    count=0
    available=~(col_mask|cross1_mask|cross2_mask)&((1<<n)-1) # 가능한 위치가 1이 되게 available 설정

    while available:
        bit=available&-available # available에서 가장 우측 1
        available-=bit # 그 우측 1을 끔(해당 자리에 퀸을 놓음)
        if row==n-1:
            count+=1
        else :
            count+=put_queen(
                col_mask|bit,
                (cross1_mask|bit)<<1,
                (cross2_mask|bit)>>1,
                row+1,n)
        
    return count



n=int(sys.stdin.readline().strip())
if n==1:
    print(1)
elif n==2 or n==3:
    print(0)
else:
    print(put_queen(0,0,0,0,n))
