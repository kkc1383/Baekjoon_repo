import sys

n=int(sys.stdin.readline().rstrip())
meeting_list=[tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

meeting_list=sorted(meeting_list, key=lambda x:(x[1],x[0])) # x[1]를 기준으로 비교, 그다음은 x[0]를 기준으로 비교, 반환은 (x[1],x[0]) 형태

count=0
last_end=0
for start,end in meeting_list:
    if start>=last_end:
        last_end=end
        count+=1
    
print(count)

# 어차피 가장 많은 회의를 하려면 양 끝에서 최대한 많이 시간을 벌어줘야함.
# 따라서 마치는 시간이 가장 빠른 회의부터 가져가는게 맞다. 왜냐면 빨리 마쳐야 남는 시간이 많으니
# 따라서 lambda함수를 이용하여 빨리 마치는 회의가 앞에오도록 정렬하고 앞에서부터 차례로 count에 더함. 회의 종료되면 종료시간 업데이트하면서 다음 회의 불러오기