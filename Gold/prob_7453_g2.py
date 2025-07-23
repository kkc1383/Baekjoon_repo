from collections import Counter
import sys

n=int(sys.stdin.readline().strip())

A=[0]*n
B=[0]*n
C=[0]*n
D=[0]*n
for i in range(n):
    A[i],B[i],C[i],D[i]=list(map(int,sys.stdin.readline().strip().split()))

count=0
ab_sum=Counter() 
for a in A:
    for b in B:
        ab_sum[a+b]+=1

count=0
get=ab_sum.get # 메소드 객체를 로컬변수에 저장. 메소드가 변수화 된거임
for c in C:
    for d in D:
        # 메소드 객체를 호출. 메소드도 그냥 객체로 만들어서 쓰는거임
        count+=get(-(c+d),0) # -(c+d)의 값을 가지면 그 카운트를 반환 없으면 0

print(count)


# 그냥 해시 카운터 쓰는게 해법이었네요 답이 없었음 시간초과 때문에
#  Counter란 해시가능한 객체의 개수를 빠르게 셀 수 있도록 만들어진 딕셔너리 서브클래스임
# gpt야 고맙다
