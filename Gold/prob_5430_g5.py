from collections import deque
import sys

n=int(sys.stdin.readline().strip())
for _ in range(n):
    command=deque(list(sys.stdin.readline().strip()))
    array_num=int(sys.stdin.readline().strip())
    array=deque(eval(sys.stdin.readline().strip()))
    right_array=[]
    illegal=False
    left_right=0 # 0이면 popleft, 배열 그대로,  1이면 popright, 배열 appendright하기
    while command:
        if command.popleft()=="R": # (left_right+1)%2로 만들기
            left_right=(left_right+1)%2
        else: # D 일때
            if not array:
                illegal=True
                break
            if left_right==0: # popleft하고 배열 그대로 사용
                array.popleft()
            else: # 
                array.pop()

    if illegal:
        print("error")
    else:
        if left_right==1:
            while array:
                top=array.pop()
                right_array.append(top)
            print('[',end="")
            print(*right_array,sep=',',end='')
            print(']')
        else: # left_right==0 일 때
            print('[',end="")
            print(*(list(array)),sep=',',end="")
            print(']')
            


# 굳이 deque를 써야할까?
# deque(list)로 바로 변환이 되네요~
# 초기화 변수는 위치 잘 확인해야합니다.
# 출력 포맷을 맞추는게 중요했음
# list를 출력할때 '[',']'를 빼는것은 list앞에ㅐ *을 붙이면 가능, 그리고 각 원소를 구분하는 구분자를 넣을때는 sep="구분자"로 하면됨