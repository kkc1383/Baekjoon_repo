import sys

n=int(sys.stdin.readline().rstrip())
num_list=list(map(int,sys.stdin.readline().rstrip().split()))

sorted_num_set=sorted(set(num_list))
num_dict={v : i for i,v in enumerate(sorted_num_set)}
for i in range(n):
    print(num_dict[num_list[i]], end=' ')


# set은 중복 원소를 제거해주지만 unordered 자료형이기 때문에 index를 찾으려면 O(n)의 탐색 시간이 필요하다.
# 따라서 python 3.7이상은 dict가 order 가 존재하고 dictionary로 매핑을 통해 탐색 시간을 O(1)로 만들어 주었다.