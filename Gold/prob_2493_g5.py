import sys

n=int(sys.stdin.readline().strip())
tower_list=list(map(int,sys.stdin.readline().rstrip().split()))
tower_stack=[]
answer_list=[]
for i in range(len(tower_list)):
    while len(tower_stack)!=0 and tower_list[i]>tower_stack[-1][0]:
        tower_stack.pop()
    
    if len(tower_stack)==0:
        answer_list.append(0)
    else:
        answer_list.append(tower_stack[-1][1]+1)

    tower_stack.append([tower_list[i],i])

print(' '.join(map(str,answer_list)))

# list랑 stack이랑 변수이름 좀 다르게 해야겠다 헷갈리고 자동완성이 자꾸 다른거 해주네