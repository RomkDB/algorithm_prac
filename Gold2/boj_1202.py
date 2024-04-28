# 백준 1202번 보석 도둑
# pypy3로 제출
import heapq as hq

n, k = map(int, input().split())
stone = []
bag = []

for i in range(n):
    weight, price = map(int, input().split())
    stone.append((weight, price))

for j in range(k):
    max_weight = int(input())
    bag.append(max_weight)

stone.sort()
bag.sort()

heap = []
cur = 0
result = 0

for x in bag:
    while cur < n:
        weight, price = stone[cur]
        if x >= weight:
            hq.heappush(heap, -price)
            cur += 1
        else:
            break
    
    if len(heap) > 0:
        price = -hq.heappop(heap)
        result += price

print(result)