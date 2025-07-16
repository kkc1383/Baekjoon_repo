import sys

n,m=list(map(int,sys.stdin.readline().rstrip().split()))

pok_list=[]
pok_dict={}
output_list=[]
for i in range(n):
    input_value=sys.stdin.readline().rstrip()
    pok_list.append(input_value)
    pok_dict[input_value]=i
for prob in range(m):
    input_value=sys.stdin.readline().rstrip()
    if input_value[0].isdigit():
        output_list.append(pok_list[int(input_value)-1])
    else:
        output_list.append(pok_dict[input_value]+1)

for elem in output_list:
    print(elem)

# 시간초과가 자꾸 나서 애먹었는데
# print 함수가 생각보다 느리다. 그래서 출력을 모아서 한번에 쓰는게 훨씬 빠름
# output_list를 만들어서 나중에 한번에 출력하는게 좋을듯
# 혹은 sys.stdout.write()를 쓰는 것도 방법임
# 그리고 isdigit()함수로 정수 판단 가능