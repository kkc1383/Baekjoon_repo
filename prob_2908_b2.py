import sys

a,b=list(sys.stdin.readline().strip().split())
wrong_a=int(a[::-1])
wrong_b=int(b[::-1])
print(max(wrong_a,wrong_b))
