# 백준 7662번 이중 우선순위 큐
import heapq as hq

def pop(heap):
    while len(heap) > 0:
        data, idx = hq.heappop(heap)

        if not delete[idx]:
            delete[idx] = True
            return data
    return None

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    cur = 0
    delete = [False] * (k + 1)
    
    for i in range(k):
        com, data = input().split()

        if com == 'I':
            hq.heappush(max_heap, (-int(data), cur))
            hq.heappush(min_heap, (int(data), cur))
            cur += 1
        elif com == 'D':
            if data == '1':
                pop(max_heap)
            elif data == '-1':
                pop(min_heap)
    
    max_val = pop(max_heap)

    if max_val == None:
        print('EMPTY')
    else:
        hq.heappush(min_heap, (-max_val, cur))
        print(-max_val, pop(min_heap))