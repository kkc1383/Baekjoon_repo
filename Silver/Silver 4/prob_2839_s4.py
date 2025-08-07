import sys

target=int(sys.stdin.readline().strip())

num_list=[3,5]

dp=[float("inf")]*(target+1)
dp[0]=0

for num in num_list:
    for i in range(1,target+1):
        dp[i]=min(dp[i],dp[i-num]+1)


print(dp[target] if dp[target]!=float("inf") else -1)


# import sys

# n=int(sys.stdin.readline().rstrip())

# def find_three(n):
#     if n%3==0:
#         return n//3
#     else:
#         return -1
# min_value=float('inf')
# three=find_three(n)
# five=0
# if three!=-1:
#     min_value=three+five
# while n>=5:
#     n-=5
#     three=find_three(n)
#     five+=1
#     if three == -1:
#         continue
#     else:
#         min_value=min(three+five,min_value)

# if min_value==float('inf'):
#     print(-1)
# else:
#     print(min_value)



#dp로 푸는방법인데 O(2^n)이어서 쓰지 않는 것이 좋다.