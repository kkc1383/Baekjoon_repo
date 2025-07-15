import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
fruits = list(map(int, sys.stdin.readline().split()))

counter = defaultdict(int)   # 윈도우 안 과일별 개수
l = 0
best = 0

for r, f in enumerate(fruits):      # 오른쪽 포인터 r 확장
    counter[f] += 1

    # 종류가 3개가 되면 조건 위반 → 왼쪽 l을 줄이며 2개로 복구
    while len(counter) > 2:
        counter[fruits[l]] -= 1 # 하나씩 줄여나가고
        if counter[fruits[l]] == 0: # 다 줄였으면
            del counter[fruits[l]] # 원소 삭제
        l += 1                     # 윈도우 왼쪽 축소

    best = max(best, r - l + 1)    # 조건 만족 시 길이 갱신

print(best)


# 슬라이드 윈도우라는 기법이고 범위를 조절하여서 빠르게 구하는 방법임
# 여기에 경우 for문을 순회하면서 오른쪽 범위를 고정하고, 종류가 3개일때만 왼쪽부터 과일 한 종류가 모두 없어질 때까지 제거
# 특이한 점은 과일의 총 갯수를 슬라이드 바의 길이로 표현 한 것임 r-l+1