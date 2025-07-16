import sys

num,amount=list(map(int,sys.stdin.readline().rstrip().split()))
coin_list=[]
for _ in range(num):
    input_value=int(sys.stdin.readline().rstrip())
    coin_list.append(input_value)

def min_coin(coin_list,amount):
    result=0
    for coin in coin_list:
        while amount>=coin:
            result+=1
            amount-=coin
    return result
    

print(min_coin(coin_list[::-1],amount))