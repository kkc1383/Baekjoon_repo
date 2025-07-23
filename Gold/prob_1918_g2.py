import sys

def prior(operator):
    if operator=="(" or operator==")":
        return 0
    elif operator=='*' or operator=="/":
        return 1
    elif operator=="+" or operator=="-":
        return 2
    return -1
    
sentence=list(sys.stdin.readline().rstrip())
operator_stack=[]
for char in sentence:
    if char=="*" or char=="/" or char=="+" or char=="-":
        if not operator_stack: # 스택에 아무것도 없으면
            operator_stack.append(char) # 아묻따 일단 넣습니다
        else: # 스택에 하나라도 있다면
            while operator_stack and prior(operator_stack[-1])<=prior(char): # 우선순위가 높은 연산자가 있다면, 안그럴때까지 계속 뽑습니다.
                if operator_stack[-1]=="(": # 왼쪽 괄호가 나오면 멈추어야 함. 왜냐면 괄호 밖은 우선순위가 낮으니까
                    break
                top=operator_stack.pop()
                print(top,end="")
            operator_stack.append(char)
    elif char=="(": # 여는괄호는 그냥 넣습니다.
        operator_stack.append(char)
    elif char==")": # 닫는괄호는 여는괄호가 나올때까지 다 빼고 출력합니다.
        while operator_stack:
            top=operator_stack.pop()
            if top=="(":
                break
            print(top,end="")
    else: # 피연산자, 문자
        print(char,end="")

while operator_stack:
    top=operator_stack.pop()
    print(top,end="")

# 왼쪽 괄호를 만나면 순회 그만 빼주지도 말아야함
# 괄호 밖에 있는 연산자는 무조건 우선순위가 낮기 때문에 먼저 꺼내면 안됨
# 따라서 괄호의 우선순위를 가장 높게 할 수 밖에 없었음. 나가지 말라고 다른 연산자는 잔말말고 쌓이라고