import sys

my_dict={}
for i in range(9):
    input_value=int(sys.stdin.readline().strip())
    my_dict[i]=input_value
max_key=max(my_dict, key=my_dict.get)
max_value=my_dict[max_key]
print(max_value)
print(max_key+1)