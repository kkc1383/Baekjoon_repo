import bisect
import sys

n=int(sys.stdin.readline().strip())
water_list=list(map(int,sys.stdin.readline().strip().split()))

water_list.sort()

base=0
left=1
right=n-1
min_value=float('inf')
min_list=[]
findzero=False
for i in range(n-2):
    base=i
    left=base+1
    right=n-1
    while left<right:
        sum_value=water_list[left]+water_list[right]+water_list[base]
        if abs(min_value)>abs(sum_value):
            min_value=sum_value
            min_list=[base,left,right]

        if sum_value==0:
            min_list=[base,left,right]
            findzero=True
            break
        elif sum_value>0: # 양수를 줄여야함
            right-=1
        else : #음수를 줄여야함
            left+=1
    if findzero:
        break

min_base,min_left,min_right=min_list
print(f'{water_list[min_base]} {water_list[min_left]} {water_list[min_right]}')

# 이건 왼쪽을 하나 아예 고정하고 두 용액을 섞는 문제와 같다.
# 그리고 하나 끝나면 왼쪽을 한칸씩 오른쪽으로 당기면 된다.
# left,right, best 선언 잘하고
# 첨에 best abs 넣어서 잘 비교하고