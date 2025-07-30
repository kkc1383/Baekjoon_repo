from collections import defaultdict, deque
import sys

test_case=int(sys.stdin.readline().strip())
for _ in range(test_case):
    start,target=list(map(int,sys.stdin.readline().strip().split()))

    can=defaultdict(list) # x라는 숫자를 만들기 위한 최소 명령어

    can[start]=[]

    myqueue=deque()
    myqueue.append(start)

    while myqueue:
        top=myqueue.popleft()

        # D 일때
        if top*2>=10000:
            next_D=top*2%10000
        else:
            next_D=top*2
        if not next_D in can:
            can[next_D].extend(can[top]+["D"])
            myqueue.append(next_D)

        # S 일때
        if top==0:
            next_S=9999
        else:
            next_S=top-1
        if not next_S in can:
            can[next_S].extend(can[top]+["S"])
            myqueue.append(next_S)

        
        # L 일때
        first_L=top//1000 # 천의 자리수
        next_L=top
        next_L*=10
        next_L%=10000
        next_L+=first_L
        if not next_L in can:
            can[next_L].extend(can[top]+["L"])
            myqueue.append(next_L)

        # R 일때
        first_R=top%10 # 일의 자리수
        next_R=top
        next_R//=10
        first_R*=1000
        next_R+=first_R
        if not next_R in can:
            can[next_R].extend(can[top]+["R"])
            myqueue.append(next_R)

        if next_R==target or next_D==target or next_L==target or next_S==target:
            print(*can[target], sep="")
            break
        

# 그다음 거에 대한건 can[next] += can[prev]+command 로 하면되지
# 해당 키 가 있는지 확인은 if key in can
# 시간초과 났었는데 그 이유는 key 있는지 확인하고 append 해야되는데 그냥 무조건 append 해버림