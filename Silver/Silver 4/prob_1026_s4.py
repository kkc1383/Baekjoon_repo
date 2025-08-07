import sys


num=int(sys.stdin.readline().strip())

list_a=list(map(int,sys.stdin.readline().strip().split()))
list_b=list(map(int,sys.stdin.readline().strip().split()))

list_a.sort()
list_b.sort(reverse=True)

sum=0
for i in range(num):
    sum+=list_a[i]*list_b[i]

print(sum)

# 그리디 알고리즘은 정렬만 잘해도 풀린다.