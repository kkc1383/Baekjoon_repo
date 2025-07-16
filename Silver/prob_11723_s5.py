import sys

n=int(sys.stdin.readline().rstrip())

num_list=[]

for _ in range(n):
    command=sys.stdin.readline().rstrip().split()

    if command[0]=='add':
        if not command[1] in num_list:
            num_list.append(command[1])
    elif command[0]=='remove':
        if command[1] in num_list:
            num_list.remove(command[1])
    elif command[0]=='check':
        if command[1] in num_list:
            print('1')
        else:
            print('0')
    elif command[0]=='toggle':
        if command[1] in num_list:
            num_list.remove(command[1])
        else:
            num_list.append(command[1])
    elif command[0]=='all':
        num_list=[str(i) for i in range(1,21)]
    elif command[0]=='empty':
        num_list=[]



## 기존에 받는 숫자들은 문자열 형태로 들어 갔는데 all의 경우 int로 들어가서 자료형의 차이 때문에 틀리게 되었음 자료형 일치