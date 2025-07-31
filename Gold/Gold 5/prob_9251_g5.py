import sys

str1=sys.stdin.readline().strip()
str2=sys.stdin.readline().strip()

LCS=[[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for y in range(1,len(str2)+1): # 왼쪽과 위를 비교해야 되기때문에 마진을 생성
    for x in range(1,len(str1)+1):
        
        # 우선 앞에서부터 비교
        if str1[x-1]==str2[y-1]: # 실제 문자열은 인덱스가 0부터 시작하기 때문에 그에 대한 처리가 필요함
            LCS[y][x]=LCS[y-1][x-1]+1 # 공통부분을 만든 시초
        else:
            LCS[y][x]=max(LCS[y-1][x],LCS[y][x-1]) # 위쪽 왼쪽에서부터 최댓값을 가져옵니다. 공통수열을 유지한다는 생각

result=[]
nx=len(str1)
ny=len(str2)
while ny>0 and nx>0:
    if LCS[ny][nx]==LCS[ny-1][nx]: # 위에 같은 값이 있다면
        ny=ny-1
    elif LCS[ny][nx]==LCS[ny][nx-1]:  # 왼쪽에 같은 값이 있다면
        nx=nx-1
    else: # 위쪽 왼쪽에 같은 값이 없다면 걔가 공통 수열에 포함 되는 문자임
        result.append(str1[nx-1]) # 아니면 str2[ny] 해도됨
        ny=ny-1
        nx=nx-1
    
print(len(result))

# 중요한점은 문자열의 길이와 LCS의 길이가 1 차이난다는 것 그리고 LCS는 1부터 유효하지만 문자열은 0부터 그래서 인덱스 관리가 중요하다