import sys

n=int(sys.stdin.readline().strip())
for i in range(n):
    input_value=list(sys.stdin.readline().strip())
    score_get=0
    total_score=0
    for elem in input_value:
        if elem=='O':
            score_get+=1
            total_score+=score_get
        else:
            score_get=0
    print(total_score)
