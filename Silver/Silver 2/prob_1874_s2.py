import sys

n=int(sys.stdin.readline().rstrip())
question_list=[int(sys.stdin.readline().rstrip()) for _ in range(n)]


top=0
num_list=[i for i in range(1,n+1)]
stack_list=[]
ops_list=[]
cur=0

for target in question_list:
    while cur<target: # 지금 stack은 cur를 들고 있다.
        stack_list.append(cur+1)
        ops_list.append('+')
        cur+=1
    
    if stack_list[-1]==target:
        del stack_list[-1]
        ops_list.append('-')
    else:
        ops_list.append('NO')
        break
    
if ops_list[-1]=="NO":
    print("NO")
else:
    for op in ops_list:
        print(op)


# 리스트로 스택을 구현하여 문제를 푼다.
# 슬라이싱이 생각보다 시간을 많이 잡아먹는 표현이었음
# 맨 끝 원소를 지우는건 list=list[:-1]로 하지 말고 del list[-1]로 하면 O(1)로 끝남