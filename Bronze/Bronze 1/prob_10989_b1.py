import sys


MAX = 10001
count = [0] * MAX

n = int(sys.stdin.readline())
for _ in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(MAX):
    for _ in range(count[i]):
        sys.stdout.write(f'{i}\n')