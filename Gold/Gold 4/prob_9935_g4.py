from collections import deque
import sys

sentence=list(sys.stdin.readline().strip())
explode=sys.stdin.readline().strip()
length=len(explode)
 
check_stack=[] # 스택이 모든 문자를 다 받아 오는것이 포인트 솔직히 sentence의 복사급이 되는 것이 필요하긴 했어
for char in sentence:
    check_stack.append(char) # 모든문자를 일단 다 받아온다.

    if len(check_stack)>=length: # 스택길이가 length보다크면 항상 확인. 그래야 스택끝나고도 다 볼수 있지.
        if ''.join(check_stack[-length:])==explode:
            for _ in range(length): # 문자 길이만큼 pop
                check_stack.pop()

answer=''.join(check_stack)
print(answer if check_stack else "FRULA")


# 시작하는 글자가 있으면 스택에 넣고
# 끝나는 글자가 있으면 하위 explode 갯수만큼 검사해서 맞으면 스택에서 제거, 이거 반복
# 모든 문자를 다 스택에 받아오는게 포인트
# 어차피 맨 끝에서만 일어나고 반복되는 것들도 한문자 한문자 받아올때마다 검사하면 되는문제
# 이제 문자열을 어떻게 조리할지도 은근히 관전포인트
# list를 str로 나타내는 방법은 ''.join(list)