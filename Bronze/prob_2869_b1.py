import sys

a,b,v=list(map(int,sys.stdin.readline().strip().split()))
result=(v-a)//(a-b)
if (v-a)%(a-b) !=0:
    result+=1
print(result+1)

