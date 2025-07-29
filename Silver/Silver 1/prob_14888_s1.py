from itertools import permutations
import sys

n=int(sys.stdin.readline().strip())
num_list=list(map(int,sys.stdin.readline().strip().split()))
add_num,sub_num,mul_num,div_num=list(map(int,sys.stdin.readline().strip().split()))

operator_list=[0]*add_num + [1]*sub_num + [2]*mul_num + [3]*div_num


max_result=-(1<<31)
min_result=(1<<31)-1
for p in set(permutations(operator_list)):
    result=num_list[0]
    num_index=1
    for oper in p:
        if oper==0: # 더하기
            result+=num_list[num_index]
        elif oper==1: # 빼기
            result-=num_list[num_index]
        elif oper==2: # 곱하기
            result*=num_list[num_index]
        elif oper == 3:
            if result < 0:
                result = -(-result // num_list[num_index])
            else:
                result = result // num_list[num_index]
        
        num_index+=1
    max_result=(result if result>max_result else max_result)
    min_result=(result if result<min_result else min_result)

print(max_result)
print(min_result)

# 메인 포인트는 순열에서 동일한 원소들을 없애는 최적화를 set()을 통해서 할 수 있었고,
# 나눗셈의 경우 어짜피 뒤에 수는 양수니까 앞 수 result만 검사해서 양수로 바꿨다가 음수로 바꿔주고
# 그냥 완전탐색하도 풀리긴하네요 원래는 백트래킹 해야 한다던데
# 아 그리고 수 정렬 하면안됩니다. 수 순서가 정해진 상태에서 최댓값을 구해야 되가지고