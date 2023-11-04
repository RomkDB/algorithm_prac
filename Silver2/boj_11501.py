# 백준 11501번 주식
t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    price = 0
    max_benefit = 0

    for i in range(len(stocks)-1, -1, -1):
        if stocks[i] > max_benefit:
            max_benefit = stocks[i]
        else:
            price += max_benefit - stocks[i]
    
    print(price)