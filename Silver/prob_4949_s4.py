import sys

line_list_arr=[]

while True:
    line=sys.stdin.readline().rstrip('\n')
    if line==".":
        break
    line_list_arr.append(line)

for line in line_list_arr:

    my_list=[]
    illigal=False
    try:
        for chr in line:
            if chr == '(' :
                my_list.append(1)
            elif chr == ')' :
                if my_list[-1]==1:
                    my_list.pop()
                else:
                    illigal=True
                    break

            if chr == '{' :
                my_list.append(2)
            elif chr == '}':
                if my_list[-1]==2:
                    my_list.pop()
                else:
                    illigal=True
                    break

            if chr == '[':
                my_list.append(3)
            elif chr == ']' :
                if my_list[-1]==3:
                    my_list.pop()
                else:
                    illigal=True
                    break
        
        if len(my_list)==0 and not illigal:
            print("yes")
        else:
            print("no")

    except IndexError:
        print("no")