import sys

def is_han(num):
    if num<=99:
        return True
    num_list=list(map(int,str(num))) # num=123, num_list=[1,2,3]
    temp=(num_list[0]+num_list[2])/2
    if temp==num_list[1]:
        return True
    else:
        return False


n=int(sys.stdin.readline().strip())
if n<=99:
    print(n)
else:
    count=99
    for i in range(100,n+1):
        if is_han(i):
            count+=1
    print(count)