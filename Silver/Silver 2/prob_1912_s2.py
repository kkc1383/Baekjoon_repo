import sys

num=int(sys.stdin.readline().strip())

num_list=list(map(int,sys.stdin.readline().strip().split()))

for i in range(1,num):
    num_list[i]=max(num_list[i],num_list[i]+num_list[i-1])

print(max(num_list))

# 어짜피 이전만 알면되기 때문에 순차적으로 num_list를 갱신해나가면됨