import sys

a,b,c=list(map(int,sys.stdin.readline().rstrip().split()))


def a_bsquare_mod_c(a,b,c):
    
    if b==1: # 탈출 조건
        return a%c
    else:
        temp=a_bsquare_mod_c(a,b//2,c)
        result=(temp*temp)%c
        if b%2!=0:
            result=(result*(a%c))%c
        return result
    
print(a_bsquare_mod_c(a,b,c))

# 분할정복의 기초는 연산양을 반씩 줄여나간다는 것이다. 이분적으로, 그래야 계산량이 n에서 logn으로 줄어듬
# 이번 문제의 착안점은 a^n%c를 (a^n/2%c) * (a^n%c) %c 의 점화식으로 바꾸어서 분할하는 방법이었다.
