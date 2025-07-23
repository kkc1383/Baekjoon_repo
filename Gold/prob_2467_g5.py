import sys

n=int(sys.stdin.readline().strip())
water_list=list(map(int,sys.stdin.readline().strip().split()))

left=0
right=n-1
best=float('inf')
best_list=[]
while left<right:
    mixed=water_list[left]+water_list[right]
    if abs(mixed)<abs(best):
        best=mixed
        best_list=[left,right]
    if mixed==0:
        best_list=[left,right]
        break
    elif mixed>0:
        right-=1
    else:
        left+=1

print(f'{water_list[best_list[0]]} {water_list[best_list[1]]}')

# 복습인가? ㅋㅋ 잘 먹고 갑니다~