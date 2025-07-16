import sys

n=int(sys.stdin.readline().rstrip())


def find(num):
    if num==0:
        return 0
    if num==1:
        return 0
    else:
        return 1+min(find(num//3)+num%3,find(num//2)+num%2)  # 나눌때(맨 앞에 있는 1) + 1을 뺄때 (modular 들)

print(find(n))