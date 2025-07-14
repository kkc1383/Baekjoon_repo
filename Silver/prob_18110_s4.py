import sys

n=int(sys.stdin.readline().rstrip())
score_list=[]
for _ in range(n):
    input_value=int(sys.stdin.readline().rstrip())
    score_list.append(input_value)
score_list.sort()

def my_round(n:float): return int(n)+(n>=int(n)+0.5)

if len(score_list)==0:
    print(0)
elif 1<=len(score_list)<=2:
    print(my_round(sum(score_list)/len(score_list)))
else:
    julsa_people=my_round(len(score_list)*0.15)
    score_list=score_list[julsa_people:-julsa_people]
    avg=my_round(sum(score_list)/len(score_list))
    print(avg)
    