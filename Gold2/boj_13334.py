# 백준 13334번 철로
import heapq as hq

n = int(input())
line = []

for i in range(n):
    start, end = map(int, input().split())

    if end < start:
        start, end = end, start
    
    line.append((start, end))

line.sort(key=lambda x: x[1])
d = int(input())
heap = []
cur = 0
result = 0

for j in line:
    start, end = j

    if end - start > d:
        continue
    
    cur = end
    hq.heappush(heap, start)
    
    while len(heap) > 0:
        start = hq.heappop(heap)

        if cur - start > d:
            continue
        else:
            hq.heappush(heap, start)
            break
    
    result = max(result, len(heap))

print(result)