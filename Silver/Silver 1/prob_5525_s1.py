
import sys

n=int(sys.stdin.readline().rstrip())
length=int(sys.stdin.readline().rstrip())
string=sys.stdin.readline().rstrip()

check=['I']+(['OI']*n)

sum_list=[]
index=0
while index<=length-2:
    seq=0
    if string[index]=='I':
        index+=1
        while index+1<length and string[index]=='O' and string[index+1]=='I':
           index+=2
           seq+=1
        sum_list.append(seq)
    else:
        index+=1

result=0
for i in sum_list:
    if i>=n:
        result+=(i+1-n)
print(result)


# 로직은 완벽했으나 범위 처리에 대한 문제가 발생하였다.
# while 문에 index+1<length를 통해 indexError 발생을 방지하였고 , 마지막 for문에 if문을 통해 음수 값이 더해지지 않도록 방지하였다.
# 패턴찾는 문제는 투포인터/슬라이딩 윈도우로 푸는게 좋다.
# from collections import deque

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# s = sys.stdin.readline().strip()

# dq = deque()          # 최근 본 문자
# cnt = 0               # 'OI' 페어 개수
# ans = 0

# for ch in s:
#     dq.append(ch)
#     if len(dq) >= 3:
#         a, b, c = dq[-3], dq[-2], dq[-1]
#         if a == 'I' and b == 'O' and c == 'I':
#             dq.pop()          # 맨 끝 'I'만 남겨 연속성 유지
#             dq.popleft()
#             cnt += 1
#             if cnt >= n:
#                 ans += 1
#         else:
#             # 패턴이 끊기면 큐 리셋
#             dq.clear()
#             if ch == 'I':
#                 dq.append(ch)
#             cnt = 0

# print(ans)