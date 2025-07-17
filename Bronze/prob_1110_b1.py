import sys

n=int(sys.stdin.readline().rstrip())

temp=n
count=0

def one_cycle(n,count): # 중점 포인트는 받은 수를 [십의 자리수, 일의 자리수] list로 변환하여 계산함
    if n<10: # 한자리 수일 경우
        num_list=[n]
        num_list.insert(0,0) # 맨 앞에 0을 추가
        # 이후 [0,n]으로 됨

        # count+=1  # 이 동작도 사이클 횟수로 칠 지 몰라 count를 했지만 예제에서 1 =>60 이므로 이 문제는 해당 동작을 사이클 횟수로 안 침

    else: # 두자리 수일 경우
        num_list=list(map(int,str(n))) # 각 자리수를 리스트화 시킴 ex) 12 = [1,2]

    n=num_list[1]*10+sum(num_list)%10 # 일의 자리수를 십의 자리수로 옮기고 각 자리수 더한 값의 일의 자리수를 가져옴 ab= [b, (a+b)%10]
    count+=1
    return [n,count]

n,count=one_cycle(n,count) # 한번은 무조건 돌아야 하기 때문에
while temp!=n: # 처음 주어진 수와 같을 때 까지
    n,count=one_cycle(n,count)

print(count)