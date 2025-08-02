import sys

given_str=sys.stdin.readline().strip()

# 우선 SA를 구하려면 함수를 3개 만들어야한다.


def stable_counting_sort(suffix_array, key_fn, t):
    length=len(suffix_array)
    bucket=[0]*(t+2)    # max_rank에 +2, -1~max_rank 까지니까
    for idx in suffix_array:
        bucket[key_fn(idx)+1]+=1 # counting하는 과정
    for i in range(1,len(bucket)):
        bucket[i]+=bucket[i-1] # 누적합으로 안정정렬을 하려고 함
    
    sorted_array=[0]*(length) # 정렬한 SA를 담을 공간
    for idx in reversed(suffix_array): # 끝에서부터 차례로
        bucket[key_fn(idx)+1]-=1 # 끝에서부터 하나 쓸거니까 
        sorted_array[bucket[key_fn(idx)+1]]=idx # 해당하는 자리 맨 오른쪽에 앉음
    
    return sorted_array


def radix_sort(suffix_array,group,t):
    """
    : param suffix_array: 정렬해야하는 SA
    : group: 비교 대상 문자의 랭크
    : t: 비교 블록
    """
    length=len(suffix_array)
    max_rank=max(group)

    suffix_array=stable_counting_sort(suffix_array,key_fn=lambda i : group[i+t] if i+t <length else -1, t=max_rank)
    suffix_array=stable_counting_sort(suffix_array,key_fn=lambda i : group[i],t=max_rank) # 여기에는 sentinel을 안넣음

    return suffix_array

def update_group(suffix_array, group, t):
    length=len(suffix_array)
    new_group=[0]*length
    rank=0
    new_group[suffix_array[0]]=0

    for k in range(1, length):
        prev, cur=suffix_array[k-1],suffix_array[k]

        prev_key=(group[prev], group[prev+t] if prev+t < length else -1)
        cur_key=(group[cur], group[cur+t] if cur+t < length else -1)
        if cur_key!=prev_key:
            rank+=1 # 덩어리가 바뀔때마다 그다음 숫자로 넘버링
        new_group[cur]=rank # new_rank 새로 만들기

    return new_group, rank

def getSA(str):
    """
    :param str: 대상 문자열
    :return : 접미사 배열 SA(사전순 나열)
    """
    length=len(str)
    suffix_array=list(range(length))
    group=[ord(char) for char in str]
    t=1 # 블락 크기

    while t<length: # t가 length보다 작을 때까지
        # 현재 랭크로 튜플 정렬
        suffix_array=radix_sort(suffix_array,group,t)

        # 새 랭크 계산
        group, max_rank=update_group(suffix_array,group,t)
        if max_rank==length-1: # 랭크가 length-1일때 그만
            break
        t<<=1
    return suffix_array

        

def getLCS(str,suffix_array):
    length=len(str)
    rank=[0]*length
    for i ,suf_i in enumerate(suffix_array):
        rank[suf_i]=i
    lcp=[0]*length
    height=0
    for i in range(length):
        if rank[i]==0:
            continue
        j=suffix_array[rank[i]-1] # SA에 이전거
        while i+height<length and j + height < length and str[i+height]==str[j+height]:
            height+=1
        lcp[rank[i]]=height
        if height:
            height-=1
    return lcp[1:]


given_SA=getSA(given_str)
result_LCS=' '.join(map(str,getLCS(given_str,given_SA)))
given_SA=[x+1 for x in given_SA] # 이게 참조가 되는 버전 이라기보다 걍 덮어쓰기긴한데
print(*given_SA,sep=" ")
print("x "+result_LCS)