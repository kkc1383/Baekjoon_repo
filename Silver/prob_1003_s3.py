import sys

n=int(sys.stdin.readline().rstrip())

def fibonacci(num):
    a,b=0,1
    for _ in range(1,num):
        a,b = b,a+b
    
    return a,b

for _ in range(n):
    num=int(sys.stdin.readline().rstrip())
    if num==0:
        a,b=1,0
    else:
        a,b=fibonacci(num)
    print(f'{a} {b}')


# 0 은 fibonacci(n-1), 1은 fibonacci(n)임을 알게 되었지만 시간초과로 피보나치를 재귀를 사용해서 해결할 순 없다고 생각은 했음
# 단서를 얻을 수 있는 것은 피보나치는 이전 두 단계를 모두 모르는 상태에서 풀어야 하기 때문에 재귀를 쓰지만(물론 다른 방법도 있지만)
# 여기는 이전 단계를 저장할 수 있기 때문에 충분히 재귀없이 풀어나갈 수 있음. line 8처럼