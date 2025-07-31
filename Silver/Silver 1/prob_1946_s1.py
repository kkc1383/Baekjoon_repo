import sys

test_case=int(sys.stdin.readline().strip())

for _1 in range(test_case):
    apply_num=int(sys.stdin.readline().strip())

    score_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(apply_num)]

    score_list.sort()

    count=1
    max_score=score_list[0][1]
    for score_1,score_2 in score_list:
        if max_score>score_2: # 다른건 더 잘하네
            count+=1
            max_score=score_2

    print(count)

    # 일단 한 과목 기준으로 줄 세워놓고 그다음껀 맨 위에가 가장 숫자가 크다고 했을 때 작아져야 채택되지 안작아지면 아웃