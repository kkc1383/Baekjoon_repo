import sys

n=int(sys.stdin.readline().rstrip())
num_list=list(map(int,sys.stdin.readline().rstrip().split()))

num_list.sort()

left=0
right=n-1
best=abs(num_list[0]+num_list[-1])
best_list=[left,right]

while left<right:
    mixed=num_list[left]+num_list[right]

    if abs(best)>abs(mixed):
        best=mixed
        best_list=[left,right]
    
    if mixed>0: # 더한 양수값을 줄여야하므로 오른쪽 커서를 왼쪽으로 이동
        right-=1
    elif mixed==0:
        best_list=[left,right]
        break
    else:
        left+=1
print(f'{num_list[best_list[0]]} {num_list[best_list[1]]}')


# 이 문제의 접근 방식을 다르게 해야한다.
# 일단 두 용액을 섞는 것이고 리스트를 정렬했으면 왼쪽끝과 오른쪽 끝은 각각 가장 큰값과 작은 값일 것이다.
# 이 두개를 더했을 때 음수거나 양수거나 둘중 하나일텐데, 양수면 수가 작아져야하니까 오른쪽 커서를 왼쪽으로 이동, 음수면 그 반대
# 커서를 이동할 때마다 합을 구해서 후보군을 저장해놓고, 혹여 합이 0이면 바로 탈출해도되므로 탈출, 혹시나 여기서 0으로 만들어지는 것 중 최대값이나 이런 조건이 있다면 여기서 멈추면 안됨
# 추가 조건이 있다면 다른 list나 dict에 저장해두었다가 사용하는 것이 해법이지 않을까 싶다.