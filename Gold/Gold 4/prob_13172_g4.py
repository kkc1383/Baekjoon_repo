import sys

n=int(sys.stdin.readline().strip())
sum_list=[]
mod_num=1000000007

def get_multi(num,exp): # 수와 지수를 받아서 수^지수 를 반환하는 함수
    if exp==0:
        return 1
    elif exp==1:
        return num
    else:
        if exp%2==0:
            half=get_multi(num,exp//2)
            return half*half%mod_num
        else:
            return num*get_multi(num,exp-1)%mod_num
        
for _ in range(n):
    N,S=list(map(int,sys.stdin.readline().strip().split()))
    # S/N을 해서 sum_list에 넣을건데 모듈러연산을 통해 정수로 바꿀거임
    # S/N=S*N^(-1)=S*N^(mod_num-2)

    temp=get_multi(N,mod_num-2)
    value=(temp*S)%mod_num
    sum_list.append(value)
print(sum(sum_list)%mod_num)

# 기저 처리할때 exp==0인것도 해야합니다.
# 연산 중간중간에 모듈러를 넣어줬어야 했음. exp%2==0 이랑 else에도