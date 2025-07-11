import sys

log_list=[] 
def hanoi(level, start, another, goal,real_level):
    if real_level<=20:
        if level==1:
            log_list.append(f"{start} {goal}")
            return 1
        count=hanoi(level-1,start,goal,another,real_level)
        log_list.append(f"{start} {goal}")
        count+=hanoi(level-1,another,start,goal,real_level)+1
    else:
        if level==1:
            return 1
        count=hanoi(level-1,start,goal,another,real_level)*2+1
    return count

n=int(sys.stdin.readline().strip())
print(hanoi(n,1,2,3,n))
if n<= 20: 
    for log in log_list:
        print(log)
