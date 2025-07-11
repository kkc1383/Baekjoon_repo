import sys

n=int(sys.stdin.readline().strip())
for i in range(n) :
    input_value=list(map(int,sys.stdin.readline().strip().split(' ')))
    group_avg=sum(input_value[1:])/input_value[0]
    over_avg_count=0
    for score in input_value[1:]:
        if score> group_avg:
            over_avg_count+=1
    ratio=over_avg_count/input_value[0]*100
    print(f"{ratio:.3f}%")