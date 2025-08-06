import sys

test_case=int(sys.stdin.readline().strip())

def comb(n,k):
    k=min(k,n-k)
    result=1
    for i in range(1,k+1):
        result=result*(n-i+1)//i
    return result

for _ in range(test_case):
    left,right=list(map(int,sys.stdin.readline().strip().split()))
    cases=right-left # cases C left
    print(comb(right,cases))
