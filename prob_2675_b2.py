import sys

n=int(sys.stdin.readline().strip())
for _ in range(n):
    input_value=list(sys.stdin.readline().strip().split(' '))
    multiple_count=int(input_value[0])
    
    str_list=list(input_value[1])
    result_str=""
    for elem in str_list:
        for i in range(multiple_count):
            result_str+=elem
    print(result_str)