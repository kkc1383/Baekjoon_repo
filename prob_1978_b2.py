from math import sqrt
import sys
a=int(sys.stdin.readline().strip())
my_list=list(map(int,sys.stdin.readline().strip().split()))
prime_count=0
for i in my_list: # 원소 숫자
    not_prime=0
    if i <= 1:
        continue
    if i==2 or i==3:
        prime_count+=1
        continue
    for j in range(2,int(sqrt(i)+1)): # 순회하면서 나눠보기 1~그 수 제곱근까지
        if i%j==0: #나누어 떨어지는 약수가 있다면
            not_prime+=1
            break
    if(not_prime==0):
        prime_count+=1
print(prime_count)