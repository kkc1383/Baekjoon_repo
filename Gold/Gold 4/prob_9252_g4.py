import sys

str1=sys.stdin.readline().strip()
str2=sys.stdin.readline().strip()

LCS=[[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for y in range(1,len(str2)+1):
    for x in range(1,len(str1)+1):
        if str1[x-1]==str2[y-1]: # 두 문자가 같으면
            LCS[y][x]=LCS[y-1][x-1]+1
        else:
            LCS[y][x]=max(LCS[y-1][x],LCS[y][x-1])

result=[]

nx=len(str1)
ny=len(str2)
while LCS[ny][nx]>0:
    if LCS[ny][nx]==LCS[ny-1][nx]:
        ny=ny-1
    elif LCS[ny][nx]==LCS[ny][nx-1]:
        nx=nx-1
    else:
        result.append(str1[nx-1])
        ny=ny-1
        nx=nx-1

if result:
    print(len(result))
    print(''.join(result[::-1]))
else:
    print(0)