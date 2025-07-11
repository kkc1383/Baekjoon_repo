from collections import defaultdict
import sys

n=int(sys.stdin.readline().strip())
my_dict=defaultdict(list)
for _ in range(n):
    input_word=sys.stdin.readline().strip()
    my_dict[len(input_word)].append(input_word)

sorted_dict=sorted(my_dict.items())
for key,value in sorted_dict:
    new_list=list(set(value))
    new_list.sort()
    for elem in new_list:
        print(elem)
