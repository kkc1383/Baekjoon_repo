import bisect
from inspect import stack
import sys

result_list=[]
input_value=sys.stdin.readline().strip()

def find_max_width(start,end,square_list):
    size=end-start
    if size==1: # 히스토그램이 하나 또는 둘로 나옴  여기에 브루트포스로 직접 너비를 구하면 됨
        if square_list[start]<square_list[end]:
            return max(square_list[start]*2,square_list[end])
        else:
            return max(square_list[start],square_list[end]*2)
    elif size==0:
        return square_list[start]
    
    mid=(start+end)//2
    left_area=find_max_width(start,mid,square_list)
    right_area=find_max_width(mid+1,end,square_list)

    # 합쳤을 때 생기는 mid_area를 계산하는 부분
    left=mid-1
    right=mid+1
    now_height=square_list[mid]
    mid_area=square_list[mid]
    while start<=left and right<=end: # 한쪽이 끝에 다다를 떄까지
        if square_list[left]<square_list[right]: # 양옆의 히스토그램중에서 큰걸 먼저 선택해야하고
            if square_list[right]<now_height: # 결국 가장 낮은 히스토그램까지 내려가야한다.
                now_height=square_list[right]
            mid_area=max(mid_area,now_height*(right-left)) # right-left인 이유는 left를 제외한 right~left사이의 히스토그램 수 이기 때문이다. left가 더 작은 경우라 포함하면 안됨
            right+=1
        else:
            if square_list[left]<now_height:
                now_height=square_list[left]
            mid_area=max(mid_area,now_height*(right-left)) # 엄밀히 따지자면 right-1 - (left-1) 이 맞는데 공식상 똑같으니 뭐
            left-=1
    while start<=left:
        if square_list[left]<now_height:
            now_height=square_list[left]
        mid_area=max(mid_area,now_height*(right-left))
        left-=1
    while right<=end:
        if square_list[right]<now_height:
            now_height=square_list[right]
        mid_area=max(mid_area,now_height*(right-left))
        right+=1
    return max(mid_area,left_area,right_area)

while input_value!='0':
    square_list=list(map(int,input_value.split()))
    result=find_max_width(1,len(square_list)-1,square_list)
    result_list.append(result)

    input_value=sys.stdin.readline().strip() # 다음줄 받아오기

for result in result_list: print(result)

# 시간 초과 인데 best를 구하는 함수에서 좀 오래걸리지 않았나 싶다. -> 스택을 써서 풀이
# 직사각형의 갯수가 100,000이라 nlogn으로 끝내야 하는데 for문은 어차피 다 돌아야 하니까 안에 연산이 logn으로 끝나야함. 이분탐색 이후에 별도 for문을 돌리지 않는 것이 중요
# stack 쓰는 문제네 이거
# 가장 위의 높이가 가장 높은 값이고 낮은 값을 만나면 해당 값이랑 같은거 나올때까지의 pop 횟수=너비가 된다.

# del square_list[0] # 첫 자리는 사각형의 갯수니까 사각형의 높이만 추출하기 위해
#     num_list=[]
#     best=0
#     for i in range(square_num):
#         if len(num_list)==0 or square_list[i]>=num_list[-1]: # 여태의 최댓값보다 크거나 같을 경우
#             num_list.append(square_list[i])
#         else: # 여태 최댓값보다 작을 경우 num보다 크거나 같은 수들은 결산
#             index=bisect.bisect_left(num_list,square_list[i]) # num보다 큰 수 중 가장 첫 번째
#             bigger_list=num_list[index:] # 날리지만 말고 그 값으로 도배를 해야 한다.
#             pop_count=0
#             while len(bigger_list)!=0:
#                 pop_count+=1
#                 top=bigger_list.pop()
#                 best=max(best,pop_count*top)
#             num_list=num_list[:index] # num_list 초기화
#             num_list.extend([square_list[i]]*(pop_count+1))

#     pop_count=0
#     while len(num_list)!=0:
#         pop_count+=1
#         top=num_list.pop()
#         best=max(best,pop_count*top)
#     result_list.append(best)
#     input_value=sys.stdin.readline().strip() # 다음줄 받아오기

    # 이분탐색으로 짰던거, 가장 큰 증가하는 수열의 길이와 비슷하게 접근
    # 하지만 bigger_list를 순회하는 과정에서 O(n^2)을 피할 수가 없었고 더 이상 최적화를 할 수 없다고 판단
    # 결국 stack을 써서 해결하는 걸로 하겠음.
    # bisect랑 stack을 같이 썼는데 역시나 list 슬라이싱은 속도가 느리다
    # list의 양쪽 끝만 상관있으면 stack이나 queue를 의심해봐라
    # 이분탐색에서 stack으로 바꾸면서 여러가지 변수명 충돌, 들어가야하는 값 등등이 섞여서 디버깅하는데 시간이 오래걸렸다.
    # 앞으로는 구조를 바꿔야할때는 세부적으로 구조를 잡고 처음부터 하는게 더 빠를 거같아서 그렇게 해봐야겠다.

        # stack으로 푸는 법
    # num_list=[] # list를 원소로 갖는 stack (높이, 현재까지의 너비)
    # best=0
    # for i in range(square_num):
    #     if len(num_list)==0 or square_list[i]>=num_list[-1][0]: # 여태의 최댓값보다 크거나 같을 경우
    #         num_list.append([square_list[i],1])
    #     else: # 여태 최댓값보다 작을 경우 num보다 크거나 같은 수들은 결산
    #         pop_count=0
    #         while len(num_list)!=0 and num_list[-1][0]>=square_list[i]:
    #             top=num_list.pop() # 최상단의 원소를 뽑음
    #             pop_count+=top[1] # 최상단 원소의 현재까지의 너비를 더함
    #             best=max(best,pop_count*top[0]) # 최상단원소를 마지막으로하는 최대 너비의 넓이를 저장
    #         num_list.append([square_list[i],pop_count+1])
    # pop_count=0
    # while len(num_list)!=0:
    #     top=num_list.pop()
    #     pop_count+=top[1]
    #     best=max(best,pop_count*top[0])
    # result_list.append(best)