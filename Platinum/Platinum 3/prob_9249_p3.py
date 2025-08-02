import sys
from typing import List

# ---------- Stable Counting Sort --------------------------------------------
def stable_counting_sort(suffix_array: List[int], key_fn, t: int) -> List[int]:
    """
    arr     : 정렬할 인덱스 목록
    key_fn  : idx -> 정수 키  (범위 -1 … K)
    K       : 키의 최댓값
    반환    : 같은 키의 원소 순서를 보존(stable)한 새 리스트
    시간복잡도 O(n + K) bucket을 채우는 반복문은 n(문자열 길이)를 따르고 bucket을 순회할때는 최대 키값인 K를 따른다. 최대키라고 해봐야 35밖에 안되지만 s보다 클수도 있기때문에 O(n+K) 거의 O(n)인 셈
    """
    length = len(suffix_array)
    bucket = [0] * (t + 2)          # +1 : sentinel(-1)용
    for idx in suffix_array:
        bucket[key_fn(idx) + 1] += 1  # key_fn에 i를 넣으면 group[i+t]값을 뱉어줍니다. +1을 하는 이유는 -1이 들어왔을 때 인덱스에 -1을 넣을 수는 없으니까 전체적으로 +1을 하는 것 나중에 쓸때 잘 쓰면 됨
    for i in range(1, len(bucket)):
        bucket[i] += bucket[i - 1]  

    sorted_array = [0] * length
    for idx in reversed(suffix_array):       # 역순 → 안정성 확보
        bucket[key_fn(idx)+1] -= 1 
        sorted_array[bucket[key_fn(idx)+1]] = idx

    return sorted_array

# bucket[]은 특정 수들이 가질 수 있는 최대 인덱스를 가지고 있다. 예를들자면 다음라운드에 0이 2개, 1이 1개 13이 2개라고하면 총 5개죠?
# 그럼 위에 누적합으로 만든 결과가 곧 bucket[0+1]=2, bucket[1+1]=3, bucket[13+1]=5 일거 아니에요
# 그러면 다음 라운드에서 SA값이 1인 친구는 최대 3등까지라는거죠 4등부터는 더 큰숫자고, SA값이 13인친구는 최대 5등
# 0 0 0 / 1 / 13 13  0등부터 있다고 치면 0은 최대 2등까지고 1은 최대 3등 13은 최대 5등까지라는겁니다. 오른쪽부터 채워않는느낌입니다.
# 그래서 안정정렬을 유지하기 위해서 최대 숫자에다가 최대 인덱스를 박아버리는겁니다. 그래서 역순으로 시작하는겁니다. 위에서부터 안쪽에 밀어넣는느낌

# 로직을 간단하게 설명하자면 정렬하고자하는 SA 배열을 받고, 정렬기준이 되는 값, 그리고 최대 키를 받습니다. 최대 키가 중요한 이유는 쓸데없이 긴 배열을 만들지 않고 딱 필요한 만큼만 배열을 만들기 위해서 그뿐입니다.
# 그리고 counting sort를 위한 배열인 bucket을 만들어주고요 정렬기준이되는 key_fn은 -1도 될수 있기 때문에 전체적으로 값+1인곳에 저장을 하려고합니다. -1~K까지기 때문에 K+2칸의 배열을 만듭니다.
# 그리고 counting sort를 시작합니다. index 0부터 시작해서 key_fn값의 빈도수를 bucket에 넣어주시면되요
# 그 다음 중요한건 안정정렬을 위해서 누적합을 사용할겁니다 그래서 왼쪽에서 오른쪽으로 차곡차곡 쌓아주시면되요. bucket[i]+=bucket[i-1]

# 그다음이 sorting과정인데 새로 sort한걸 받는 배열 만들어주시구요 그다음 SA의 index를 역순으로 넣습니다. 그 이유는 누적합을 이용해 안정정렬을 하기 위함이죠
# 그래서 index끝값부터 시작해서 bucket에서 내껄 찾아가지고 자리 배정받으시면 됩니다. 본인이 해당하는 key값에 최대값을 반환해줄거에요 거기가 본인 자립니다.
# 그렇게 순서에맞추어 차곡차곡 쌓아가면 sorting 완료

# ---------- Radix Sort 한 라운드 --------------------------------------------
def radix_sort(suffix_array: List[int], group: List[int], t: int) -> List[int]:
    """
    (group[i], group[i+t]) 튜플을 두 번의 안정 카운팅 정렬로 O(n)에 정렬
    t를 2배씩 해서 탐색하기때문에 logN번하는거라서 SA 총정렬이 O(nlogn)이다.
    """
    length = len(suffix_array)
    max_rank = max(group)           # 0 … n-1

    # ① 뒤쪽 키(second) 기준 정렬 이거 하나가 O(n)으로 끝남
    suffix_array = stable_counting_sort(
        suffix_array,
        key_fn=lambda i: group[i + t] if i + t < length else -1, # lambda함수를쓰면 앞에있는 i빼고 나머지는 다 기억하고 있음 t나 length나 group이나
        t=max_rank
    )
    # ② 앞쪽 키(front) 기준 정렬
    suffix_array = stable_counting_sort(
        suffix_array,
        key_fn=lambda i: group[i],
        t=max_rank
    )
    return suffix_array

# 왜 뒤쪽 키 기준으로 정렬 먼저하고 그다음 앞쪽 키 기준으로 정렬하는거지?
# 두번쨰 우선순위를 먼저 정렬하고 그 다음 첫번째 우선순위로 정렬해야 stable이 되는건가
# 위 말이 맞음
# 왜 key=lambda i : (group[i],group[i+t])를 하지 않느냐면
# 위와 같이 쓰게 되면 시간복잡도가 O(n logn^2)가 되고 그 이유는 한 라운드당 O(logn)이고 파이썬 timsort는 O(nlogn)이기 때문
# 위와 같이 나눠서 안정정렬 로하면 이전 정렬의 결과를 이용하기 때문에 O(n)으로 정렬이 가능하다
# max_rank를 받는 이유는 계산 수와 배열의 크기를 줄이기 위해서 지금 내가 계산하고자 하는 문자열에서 나올 수 있는 최대키 까지만 사용하는거임

# ---------- Group(랭크) 갱신 -----------------------------------------------
def update_group(suffix_array: List[int], group: List[int], t: int):
    """
    sa      : 현재 정렬된 접미사 인덱스
    group   : 이전 라운드 랭크
    t       : 이번 라운드 블록 길이
    return  : (새 group[], 최대 랭크 값)
    """
    length = len(suffix_array)
    new_group = [0] * length
    rank = 0
    new_group[suffix_array[0]] = 0 # suffix_array[0]는 제일 최솟값이니까 그 다음 그룹에도 무조건 최솟값임.

    for k in range(1, length): # 그냥 덩어리가 총 몇개인지 보는거임
        prev, cur = suffix_array[k - 1], suffix_array[k] # SA의 이전값 지금값
        # SA가 정렬되어있으니까 위에서부터 내려오면서 t단계일때 맨 앞 글자가 같은지, 바뀌는지 확인
        # 튜플자체를 확인하는 이유는, 그다음 글자가 우연찮게 전 단계의 다른 문자열과 같을 수 있으므로 지금 나와 속해있는 그룹중에서 다음 단계도 같아야지 같은 그룹임을 알 수 있다.
        # 그리고 지금 이 함수에서 고하는건 다음 단계를 갔을 때 바뀌는 덩어리의 갯수를 구하는거임.
        # 그리고 최신화된 SA별 다음 문자이기도하고
        prev_key = (group[prev], group[prev + t] if prev + t < length else -1)
        cur_key  = (group[cur],  group[cur  + t] if cur  + t < length else -1)
        if cur_key != prev_key:     # 키가 달라지면 랭크+1
            rank += 1
        new_group[cur] = rank
        # 그냥 그 특정 문자 값들을 덩어리 번호로 매핑시켜서 단순화 한것임.
        # 그니까 나올 수 있는 문자가 a,b,n이면 0,1,13이렇게 매기는데 counting sort 할때마다 13개의 배열을 만들지 말고 차라리 덩어리의 번호로 매겨서 추적하는게 낫다 이말임
        # 그리고 덩어리를 나누는 기준은 현재 덩어리가 같고 다음 덩어리도 같으면 같은 덩어리 아니면 빠이빠이 그리고 빠이빠이 좀 빨리하라고 일부러 1,2,4 이렇게 띄워서 하는 거임
    return new_group, rank          # rank == n-1 이면 모든 랭크 고유

# ---------- 메인 함수 --------------------------------------------------------
def SA_sort(str: str) -> List[int]:
    """
    :param s: 대상 문자열 (아스키/유니코드 모두 가능)
    :return : 접미사 배열 SA  (사전순 인덱스 나열)
    """
    length = len(str)
    suffix_array = list(range(length))
    group = [ord(char) for char in str]     # 초기 랭크 = 문자 코드
    t = 1            # 블록 길이 1,2,4,...

    while t < length: # 앞에서 t만큼 제외한거 정렬하는거라고 보면 됨
        # 1) 현재 랭크로 튜플 정렬
        suffix_array = radix_sort(suffix_array, group, t)
        # 2) 새 랭크 계산
        # max_rank란 덩어리 갯수를 말하는겁니다.
        group, max_rank = update_group(suffix_array, group, t)
        if max_rank == length - 1:       # 모든 접미사가 고유 랭크 → 완료
            break
        t <<= 1           # 블록 두 배
    return suffix_array # 정렬이 완료된 sa

# 우선 radix_sort가 뭘하는 함수인지, 왜 하는지를 알아야함
# update_group도 마찬가지고


# ---------- LCP 배열: Kasai O(n) -------------------------------------
def lcp_array(str: str, suffix_array: List[int]) -> List[int]:
    """
    Kasai 알고리즘 - 접미사 배열로부터 LCP 배열(높이 배열) 생성
    lcp[i] = SA[i]와 SA[i-1]의 Longest Common Prefix 길이
    """
    length = len(str)
    rank = [0] * length
    for i, suf_i in enumerate(suffix_array):
        rank[suf_i] = i
    lcp = [0] * length
    height = 0
    for i in range(length):
        if rank[i] == 0:            # SA 맨 앞은 LCP 정의 X (0)
            continue
        j = suffix_array[rank[i] - 1]
        while i + height < length and j + height < length and str[i + height] == str[j + height]: # 실제로 같은지 확인
            height += 1
        lcp[rank[i]] = height
        if height:  # 시간을 줄이려고 다음 케이스는 height-1부터 시작함
            height -= 1
    return lcp[1:]                  # 편의상 SA[1:] 과 대응하는 길이 반환

def getLCP(str1: str, str2: str) -> tuple[int, List[str]]:
    """
    두 문자열 a, b 의 (길이, 모든 LCS 목록)을 반환
    """
    if not str1 or not str2:
        return 0, []

    separator = chr(0)                    # 아스키 0x00 (두 문자열에 없다고 가정)
    str_12   = str1 + separator + str2
    suffix_array  = SA_sort(str_12)
    lcp = lcp_array(str_12, suffix_array)          # 길이 n-1

    length_str1 = len(str1)
    max_len = 0
    substrings = set()

    for i in range(1, len(suffix_array)):
        i1, i2 = suffix_array[i-1], suffix_array[i]
        # 하나는 a 영역(0..n_a-1), 다른 하나는 b 영역(n_a+1..)
        if (i1 < length_str1) != (i2 < length_str1):
            cur_lcp = lcp[i-1]      # LCP 배열은 SA[i-1]·SA[i] 의 공통 길이
            if cur_lcp == 0:
                continue
            if cur_lcp > max_len:
                max_len = cur_lcp
                substrings = {str_12[suffix_array[i]: suffix_array[i] + cur_lcp]}
            elif cur_lcp == max_len:
                substrings.add(str_12[suffix_array[i]: suffix_array[i] + cur_lcp])

    return max_len, sorted(substrings)

str1=sys.stdin.readline().strip()
str2=sys.stdin.readline().strip()
ans_len,ans=getLCP(str1,str2)

print(ans_len)
print(*ans)