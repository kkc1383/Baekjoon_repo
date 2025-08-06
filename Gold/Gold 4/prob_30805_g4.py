import bisect
import sys

seq1_num=int(sys.stdin.readline().strip())

seq1_list=list(map(int,sys.stdin.readline().strip().split()))

seq2_num=int(sys.stdin.readline().strip())

seq2_list=list(map(int,sys.stdin.readline().strip().split()))

ans_list=[]

common=set(seq1_list)&set(seq2_list)

while common:
    common_max=max(common)
    
    index1=seq1_list.index(common_max)
    index2=seq2_list.index(common_max)

    ans_list.append(common_max)

    seq1_list=seq1_list[index1+1:]
    seq2_list=seq2_list[index2+1:]
    
    common=set(seq1_list)&set(seq2_list)

print(len(ans_list))
if ans_list:
    print(*ans_list,sep=" ")


#현타온다... 제일 비효율적이라고 생각했던 풀이가 오히려 맞았던거다...
# 테케 크기가 작기 때문에 O(n^2)도 여유로웠음
# 최댓값을 순회중에 알 수 없다는게 어려움이었는데 그냥 최댓값 박고 시작하네
# 슬라이싱도 그냥 쓰고 시간을 널널하게 써서 이런 방식은 생각못했던 것 같다.
# 공통부분 데리고와서 그중에 max찾고 각 index알아내서 그 다음부터 슬라이싱해서 이거 반복하는거
# 진짜 직관 그자체