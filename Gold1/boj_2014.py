# 백준 2014번 소수의 곱
# pypy3로 제출함
import heapq
import copy

k, n = map(int, input().split())
p_num = list(map(int, input().split()))
hq_list = copy.deepcopy(p_num)
ck = set()

heapq.heapify(hq_list)
cnt = 0

while cnt < n:
    mn = heapq.heappop(hq_list)

    if mn in ck:
        continue
    cnt += 1
    ck.add(mn)

    for i in p_num:
        if mn * i < 2 ** 32:
            heapq.heappush(hq_list, mn*i)

print(mn)