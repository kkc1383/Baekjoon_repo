import sys

n=int(sys.stdin.readline().strip())
if n==0:
    print(1)
elif n==1:
    print(1)
elif n==2:
    print(2)
    
else:
    result=1
    for i in range(n,1,-1):
        result*=i
    print(result)