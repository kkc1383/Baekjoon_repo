import sys

n,k=list(map(int,sys.stdin.readline().strip().split()))

num=sys.stdin.readline().strip()

num_stack=list(num)

num_stack.reverse()

big_stack=[]
delete_num=k
while len(num_stack)!=0:
    top=num_stack.pop()
    if len(big_stack)==0:
        big_stack.append(top)
    else:
        if big_stack[-1] < top and delete_num>0: # big_stack의 최상단 값보다 큰게 올때, 갱신이 필요할 때 그리고 빼기 수가 남아 있을 때
            while len(big_stack)!=0 and delete_num>0 and big_stack[-1]<top:
                big_stack.pop()
                delete_num-=1
            big_stack.append(top)
        else: # 최상단 값보다 작거나 같은게 올 때 혹은 빼기 수를 다 써버렸을 때
            big_stack.append(top)

if delete_num!=0:
    for i in range(delete_num):
        big_stack.pop()

print(''.join(big_stack))

# 수의 앞에서부터 스택에 쌓는데, 다음 자리수가 이전 자리수보다 크면 삭제하는 로직입니다.
# 가장 큰 수를 찾아야되서 가장 왼쪽에 있는 수부터 삭제를하고
# 혹여 다 만들어지고 나서도 삭제해야하는 수가 남아 있다면 오른쪽에서부터 삭제합니다.
# 왜냐하면 젤 왼쪽이 가장 큰 수 일테니까요