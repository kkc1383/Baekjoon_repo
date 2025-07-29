import sys

n=int(sys.stdin.readline().rstrip())
coord_list=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

coord_list.sort(key=lambda x : x[0]) # x좌표를 기준으로 정렬합니다.

def find_min_dist(start,end):
    size=end-start # size는 탐색하고자하는 x좌표의 갯수
    if size==2: # 좌표가 두개밖에 없을 경우
        dist=(coord_list[start][0]-coord_list[end-1][0])**2+(coord_list[start][1]-coord_list[end-1][1])**2 # 두 좌표의 거리 계산
        return dist
    elif size<2: # 좌표가 하나일 경우 탐색하지 않도록
        return float('inf')
    
    mid= (start+end)//2

    left=find_min_dist(start,mid) 
    right=find_min_dist(mid,end)

    min_dist=min(left,right)

    check_list=[] # 추가로 최솟값을 체크해볼만한 후보군
    mid_x=coord_list[mid][0] # 분할한 기준 선의 x 좌표

    for i in range(start, end):
        if (coord_list[i][0]-mid_x)**2<min_dist:
            check_list.append(coord_list[i])
    
    check_list.sort(key=lambda x: x[1]) # y좌표로 정렬
    for i in range(len(check_list)-1):
        for j in range(i+1,len(check_list)):
            if (check_list[i][1]-check_list[j][1])**2>=min_dist: # 두 좌표의 y차가 min_dist보다 크거나 같아버리면 생각할 필요도 없이 break 이후의 나오는 원소들도 y좌표 기준 오름차순정렬했기 때문에 더 볼것도 없음.
                break
            dist=(check_list[i][0]-check_list[j][0])**2+(check_list[i][1]-check_list[j][1])**2
            min_dist=min(min_dist,dist)
    return min_dist

print(find_min_dist(0,len(coord_list)))