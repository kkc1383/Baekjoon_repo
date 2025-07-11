import sys

a=int(sys.stdin.readline().strip())
b=int(sys.stdin.readline().strip())
c=int(sys.stdin.readline().strip())

result=a*b*c
my_dict={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
arr=list(map(int,str(result)))
for num in arr:
    my_dict[num]+=1
 
for key,value in my_dict.items():
    print(value)