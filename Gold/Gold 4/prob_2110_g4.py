import sys

n,c=list(map(int,sys.stdin.readline().rstrip().split()))

house_list=[int(sys.stdin.readline()) for _ in range(n)]
  
house_list.sort()

def isPass(gap,total_count):
    start=0
    count=0
    while count<total_count:  # total_count번 만큼 반복
        best=0
        left=start+1
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if (house_list[start]+gap)<=house_list[mid]:
                best=mid
                right=mid-1
            else:
                left=mid+1
        if best==0:
            return False
        start=best
        # 최적의 best를 찾아냄 걔를 start로 바꿈
        count+=1
    return True

gap_left=1
gap_right=house_list[-1]-house_list[0]
gap_best=0
while gap_left<=gap_right:
    gap_mid=(gap_left+gap_right)//2
    if isPass(gap_mid,c-1):
        gap_best=gap_mid
        gap_left=gap_mid+1
    else:
        gap_right=gap_mid-1
print(gap_best)

# 이 문제는 결국 이분탐색을 두번하는 것입니다. 첫번째로는 gap(정답)에 대해 이분탐색을 통해 최댓값을 찾는 것이고, 두번째로는 왼쪽 원소+gap보다 큰 최솟값을 찾는 것입니다.(그래야 조밀하게 공유기를 설치 할 수 있으니)
# 이분탐색을 구현할수 있는 좋은 문제인것 같음
# 이분탐색을 구현하기 위해서 필요한 것, left,right로 범위 지정, mid를 통해 가운데 값 비교, best를 통해 후보군 설정, 조건 만족여부에 따라 다음 연산할 반토막의 위치를 지정(왼,오)