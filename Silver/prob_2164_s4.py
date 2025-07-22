import sys

n=int(sys.stdin.readline().rstrip())

num_list=[0,1,2]

remem_two=2
count=0
for i in range(3,500001):
    if i==remem_two*2:
        num_list.append(i)
        remem_two*=2
        count=0
    else:
        count+=2
        num_list.append(count)

print(num_list[n])

# 편법이긴한데 2의 제곱수가 아니면 2씩 늘어나고 2의 제곱수가되면 다시 초기화 되고 다음 제곱수가 나올 때까지 계속 2씩 늘어남
# 1:1, 2:2, 3:2, 4:4, 5:2, 6:4:, 7:6, 8:8

# queue로 푸는 정석
# from collections import deque
# import sys

# n=int(sys.stdin.readline().strip())

# myqueue=deque()
# for i in range(1,n+1):
#     myqueue.append(i)

# count=0
# while len(myqueue)>1:
#     if count%2==0: # 맨 앞에 수 버리기
#         myqueue.popleft()
#     else:
#         top=myqueue.popleft()
#         myqueue.append(top)
#     count+=1
# print(myqueue[0])
