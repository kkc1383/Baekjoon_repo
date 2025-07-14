from math import sqrt
import sys

def isPrime(n : int):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    else:
        is_prime=True
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                is_prime=False
                break
        return is_prime

m,n=list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(m,n+1):
    if isPrime(i):
        print(i)