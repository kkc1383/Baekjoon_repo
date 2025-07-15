import sys

n=int(sys.stdin.readline().rstrip())

def find_three(n):
    if n%3==0:
        return n//3
    else:
        return -1
min_value=float('inf')
three=find_three(n)
five=0
if three!=-1:
    min_value=three+five
while n>=5:
    n-=5
    three=find_three(n)
    five+=1
    if three == -1:
        continue
    else:
        min_value=min(three+five,min_value)

if min_value==float('inf'):
    print(-1)
else:
    print(min_value)

# def find(n):  
#     if n<0:
#         return float('inf')
#     elif n==0:
#         return 0
#     else:
#         return min(find(n-5),find(n-3))+1

# print(find(n))

#dp로 푸는방법인데 O(2^n)이어서 쓰지 않는 것이 좋다.