import sys

n=int(sys.stdin.readline().strip())
my_list=[int(sys.stdin.readline().strip()) for _ in range(n)]
my_list.sort()
for elem in my_list: print(elem)