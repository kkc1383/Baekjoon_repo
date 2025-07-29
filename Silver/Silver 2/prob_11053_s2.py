import bisect
import sys

n=int(sys.stdin.readline().strip())
num_list=list(map(int,sys.stdin.readline().rstrip().split()))
num_lower_bound=[num_list[0]] # index는 해당 원소까지의 가장 큰 증가부분수열의 길이이다. value는 가장 큰 값이고

for i in range(1,n):
    if num_list[i]>num_lower_bound[-1]:
        num_lower_bound.append(num_list[i])
    else:
        index=bisect.bisect_left(num_lower_bound,num_list[i])
        num_lower_bound[index]=num_list[i]

print(len(num_lower_bound))

# 이게 이분탐색으로 푸는 방법
# 이분탐색이라고 해봐야 내장함수 쓰는거지만...
# 착안점은 뭐냐면 각 인덱스 별로 가능한 최대의 증가하는 수열의 길이를 저장하는 거임
# 그래서 저장한 수의 맨 마지막값 list[-1]와 해당 num_list[i]를 비교해서 크면 list에 append하는거고 작다면 bisect_left를 통해 그 값보다 이상인 첫 원소와 자리 교체를 한다.
# 이걸 교체하는 이유가 뒤에 더 많은 경우를 담기 위해서인데 단박에 이해가 잘 안되긴 할 것이다.
# 그래서 이해하기 쉽게 따로 배열을 만들어서 보여주는게 편하지 싶은데 따로 포스팅해서 정리해놔야겠다.


# dp = [1]*n
# for i in range(n):
#     for j in range(i):
#         if num_list[j] < num_list[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

# dp로 푸는 방식