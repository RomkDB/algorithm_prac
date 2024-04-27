# 백준 17521번 Byte Coin
n, w = map(int, input().split())
price = []

for i in range(n):
    price.append(int(input()))

for j in range(n-1):
    if price[j] < price[j+1]:
        cnt = w // price[j]
        w += cnt * (price[j+1] - price[j])

print(w)