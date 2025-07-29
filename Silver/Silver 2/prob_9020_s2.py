import sys
from math import sqrt

def is_prime_number(num):
    not_prime=0
    for i in range(2,int(sqrt(num)+1)): # 순회하면서 나눠보기 1~그 수 제곱근까지
        if num%i==0: #나누어 떨어지는 약수가 있다면a
            not_prime+=1
            break
    if(not_prime==0):
        return True
    else:
        return False

n=int(sys.stdin.readline().strip())
for _ in range(n):
    num=int(sys.stdin.readline().strip())
    small=num//2
    
    for i in range((num//2)-1):
        small=num//2-i
        big=num-small
        if is_prime_number(small) and is_prime_number(big):
            print(f'{small} {big}')
            break
