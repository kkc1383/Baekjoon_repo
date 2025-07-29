import sys

n=int(sys.stdin.readline().strip())

two_count=0
five_count=0
for i in range(1,n+1):
    while i%2==0 and i>1:
        two_count+=1
        i/=2
        
    while i%5==0 and i>1:
        five_count+=1
        i/=5

print(min(two_count,five_count))