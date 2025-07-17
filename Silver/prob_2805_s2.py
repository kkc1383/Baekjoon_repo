import sys

num,target=list(map(int,sys.stdin.readline().strip().split()))
num_list=list(map(int,sys.stdin.readline().strip().split()))

left=0
right=max(num_list)
best=0 # 후보 저장
while left<=right:  # 교차되기 전까지
    mid=(left+right)//2
    cut_sum=sum(h-mid for h in num_list if h > mid)
    if cut_sum>=target: # 나무가 충분하지만 더 높은 절단기 길이를 위해서 다음으로 양도 지금 값은 후보군에 등록
        best=mid
        left=mid+1
    else:
        right=mid-1
print(best)

#시간초과 남 -> 이분 탐색을 통해 cut_sum을 찾아야 한다.
# 이분탐색의 단서, 숫자범위(list가 모두 숫자)+단조성(cut이 커지면 cut_sum은 작아진다)+경계값(target)
# cut_sum==target라고 해서 바로 답을 반환해버리면 안된다 더 큰 cut에서도 그 조건을 만족 할수 있기 때문에
# 이분탐색 문제의 주 성질은 조건을 만족하는 범위는 넓으나 그 중 최댓값을 구하라고 한다. 그러면 후보군을 등록해놓고 다음 단계로 나아가면 된다.
# left를 min으로 둔 탓에 틀렸습니다가 나온다. 나무 길이에 비해 더 많은 양을 요구할수도 있기 때문에 left는 0부터 시작하는 것이 맞음
# cut_sum=0
# for h in num_list:
#     if h>mid:
#         cut_sum+=(h-mid)
# 윗줄 보다 cut_sum=sum(h-mid for h in num_list if h > mid) 이게 훨씬 빠름 한줄로 쓰는게
# 왜그렇냐면 cut_sum+=같은 연산도 줄어들고 C로 번역되어 돌아가기 때문에 for를 쓰면 원소 하나하나 마다 수십개 바이트코드를 해석한다.
# 반면 sum()은 내부 while 루프를 c에서 돌며 값을 받아 누적하므로 전체가 c로 넘어가서 빠른 것임.