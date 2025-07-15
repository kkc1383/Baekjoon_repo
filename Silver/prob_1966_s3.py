import sys

n=int(sys.stdin.readline().rstrip())

for _ in range(n):
    num,priority=list(map(int,sys.stdin.readline().rstrip().split()))
    priority_list=list(map(int,sys.stdin.readline().rstrip().split()))

    index_prior_list=[]
    for i in range(num):
        index_prior_list.append([i,priority_list[i]])  # [index,priority]의 list를 list화 함
    max_priority=max(priority_list) #priority 중에 가장 큰 값
    pop_list=[]
    while True:
        if index_prior_list[0][1]==max_priority: # 맨 앞 요소의 중요도가 가장 높은 중요도 일 때
            pop_list.append(index_prior_list[0])  # pop리스트에 추가
            index_prior_list=index_prior_list[1:] # [index,priority] list의 맨 앞을 지움
            priority_list.remove(max_priority) # priority_list에서 최댓값이었던 원소를 지움
            if len(index_prior_list)==0: # 다 내보냈으면 반복 끝
                break
            max_priority=max(priority_list)  # 그 다음 최댓값을 max_priority에 저장

        else: # 맨 앞의 요소가 가장 큰 중요도가 아닐 때
            temp=index_prior_list[0] # 맨 앞 요소를 임시 저장
            index_prior_list=index_prior_list[1:] # 맨 앞 요소를 제거
            index_prior_list.append(temp) # 맨 앞 요소였던 것을 맨 뒤로 이동
    
    for index in range(len(pop_list)): # pop_list에서 찾고자 했던 index를 찾음
        if priority==pop_list[index][0]:
            print(index+1)

# 이 문제는 문제를 이해하는데 시간이 상당해 오래 걸렸고 queue의 개념이지만 list를 활용하여 문제를 충분히 풀 수 있었음.
# 여기서 키 포인트는 2차원 list를 만들어서 처음 배열의 index와 priority를 연관지어 유지하는 것이 중요함