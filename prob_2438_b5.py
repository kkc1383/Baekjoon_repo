import sys
a=int(sys.stdin.readline())
for i in range(a):
    for j in range(i+1):
        print('*',end='')
    print('')