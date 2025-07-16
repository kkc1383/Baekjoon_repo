from collections import defaultdict, deque
import sys

computer=int(sys.stdin.readline().rstrip())
pair=int(sys.stdin.readline().rstrip())
pair_dict=defaultdict(list)
for _ in range(pair):
    start,end=list(map(int,sys.stdin.readline().rstrip().split()))
    pair_dict[start].append(end)
    pair_dict[end].append(start)

check_list=deque()
check_list.append(1)
visited=[1]
result=0
while len(check_list)>0:
    start=check_list.popleft()
    for elem in pair_dict[start]:
        if not elem in visited:
            visited.append(elem)
            check_list.append(elem)
            result+=1

print(result)

# 여러가지 틀림 포인트가 있었는데 defaultdict(list)를 통해서 list를 초기화 함으로써 초기 선언이 안된 상황에서도 append함수를 통해 추가할수있었음
# visited.append(elem)이 for문 밖에 있었는데(while문 마지막) 내부적으로 pair를 돌다가 중복되는게 있을 수도 있어서 deque에 넣자마자 바로 visited에 추가하는게 맞음
# 문제에서 단뱡향이 아니고 양방향으로 의도 했기 때문에 4 1 이라도 1과 4가 연결된걸로 알고 있어야함. 어차피 visited로 중복은 안됨