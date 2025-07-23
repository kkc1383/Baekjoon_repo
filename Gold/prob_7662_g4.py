from collections import defaultdict
import heapq
import sys

input_num=int(sys.stdin.readline().strip())

for _ in range(input_num):
    max_heap=[]
    min_heap=[]
    live_dict=defaultdict(int) # 살아있는 값을 key로하는 원소는 1 죽었으면 0
    operate_num=int(sys.stdin.readline().strip())
    for i in range(operate_num):
        command=list(sys.stdin.readline().strip().split())
        if command[0]=="I":
            input_value=int(command[1])
            heapq.heappush(max_heap,-input_value)
            heapq.heappush(min_heap,input_value)
            live_dict[input_value]+=1
        elif command[0]=="D":
            if command[1]=="-1": # 최솟값 삭제
                if not min_heap:
                    continue
                while min_heap: # 살아있는 원소가 나올 때까지
                    top=heapq.heappop(min_heap)
                    if live_dict[top]>0:
                        live_dict[top]-=1
                        break
            elif command[1]=="1": # 최댓값 삭제
                if not max_heap:
                    continue
                while max_heap: # 살아있는 원소가 나올 때까지
                    top=-heapq.heappop(max_heap)
                    if live_dict[top]>0:
                        live_dict[top]-=1
                        break
    
    #끝나고 더미값들을 다 없애서 정리
    while max_heap and live_dict[-max_heap[0]]==0:
        heapq.heappop(max_heap)
    while min_heap and live_dict[min_heap[0]]==0:
        heapq.heappop(min_heap)
    
    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(f'{-max_heap[0]} {min_heap[0]}')

# 살아있는 원소에 대해서 dict로 관리
# 그러면 해야할 것은 원소가 비어있는지는 어떻게 확인하는거지?
# max_heap이나 min_heap 사이사이에 더미가 끼어 있을 수 있으니 하나라도 없어야 empty(왜냐면 둘다 한개의 힙을 대표하기 때문에)
# live_dict를 -1하는것은 실제 살아있는 원소일때만 해야했음

# 메인 아이디어는 최소힙, 최대힙에 각각 원소를 넣어 최댓값, 최솟값을 부를때 각각의 힙에서 뺴도록
# 근데 문제는 최솟값을 구하려고 최소힙에서 빼버리면 최대힙에는 반영이 안됨, 이걸 더미 값이라고 하는데 그걸 어떻게 빼주는지가 중요함
# 어떻게 빼냐면 dict를 사용하여서 빼준다. 여기서 중복값에 대비하기 위해 갯수를 저장하는걸로 해야함
# 그래서 정리할때 최소힙, 최대힙의 루트에는 반드시 살아있는 값만이 저장되도록 검사하기전에 매번 정리해야함
# 비었는지 확인은 어차피 최소힙, 최대힙이 실제 힙보다 컸으면 컸지 작진 않기 때문에 "정리 후" 하나라도 비어있으면 실제 힙은 빈것임