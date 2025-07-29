import sys

n,m=list(map(int,sys.stdin.readline().rstrip().split()))

num_list=list(map(int,sys.stdin.readline().rstrip().split()))

prefix_sum=[0]*(n+1)
prefix_sum[0]=num_list[0]
for i in range(1,n): # 여기서 포인트 전 구간을 다 구해야 점화식으로 이중 반복 돌지 않으면서 다 구할 수 있음.
    prefix_sum[i]=prefix_sum[i-1]+num_list[i]

for _ in range(m):
    start,end=list(map(int,sys.stdin.readline().rstrip().split()))
    sum_area=prefix_sum[end-1]-prefix_sum[start-1]+num_list[start-1]
    print(sum_area)

# 누적합이라는것은 0번째에서 i번째까지의 배열의 합을 prefix_sum[i]로 나타내고 이는 O(n)으로 구할 수 있다.
# 그다음 원하는 start, end를 통해 prefix_sum[end]-prefix_sum[start]를 하면 끝
# 누적합 관련 문제들은 슬라이딩 윈도우나, 이 방식(누적합을 다 구해놓고 뺴기 방식)을 사용하면 좋을 듯