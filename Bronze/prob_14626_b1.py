import sys

isbn_list=list(sys.stdin.readline().strip())
isbn_list_no_m=isbn_list[:-1]
m=int(isbn_list[-1])

sum_weight=0
star_index=0
for i in range(len(isbn_list_no_m)):
    if isbn_list[i]=='*':
        star_index=i
        continue
    if i%2 ==0:
        sum_weight+=int(isbn_list_no_m[i])
    else:
        sum_weight+=int(isbn_list_no_m[i])*3
sum_weight+=m

for i in range(10):
    if star_index%2==0:
        if (sum_weight+i)%10==0:
            print(i)
            break
    else:
        if (sum_weight+i*3)%10==0:
            print(i)
            break