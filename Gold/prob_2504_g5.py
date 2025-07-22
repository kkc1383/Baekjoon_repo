import sys

my_list=list(sys.stdin.readline().rstrip())
my_list.reverse()
my_stack=[] # (괄호값,결산된 값)
answer=0
while len(my_list)!=0:
    top=my_list.pop()
    if top==')' and len(my_stack)!=0:
        if my_stack[-1][0]!=2: # 괄호가 열려있지 않으면
            answer=0
            break
        stack_top=my_stack.pop()
        if len(my_stack)==0: # 더이상 부모가 없을 경우
            if stack_top[1]==0: # 자식이 없었을 경우
                answer+=2
            else: # 자식이 있었을 경우
                answer+=stack_top[1]*stack_top[0]
        else: # 부모가 남아 있을 경우 부모의 결산값에 본인 결과 값을 추가
            if stack_top[1]==0:
                my_stack[-1][1]+=2
            else:
                my_stack[-1][1]+=stack_top[1]*stack_top[0]
    elif top==']'and len(my_stack)!=0:
        if my_stack[-1][0]!=3: # 괄호가 열려 있지 않으면
            answer=0
            break
        stack_top=my_stack.pop()
        if len(my_stack)==0: # 더이상 부모가 없을 경우
            if stack_top[1]==0:
                answer+=3
            else:
                answer+=stack_top[1]*stack_top[0]
        else:
            if stack_top[1]==0:
                my_stack[-1][1]+=3
            else:
                my_stack[-1][1]+=stack_top[1]*stack_top[0]
    elif top=='(':
        my_stack.append([2,0])
    elif top=='[':
        my_stack.append([3,0])
    else:
        answer=0
        break
if len(my_stack)!=0:
    answer=0
print(answer)