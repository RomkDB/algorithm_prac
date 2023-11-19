# 백준 11279번 최대 힙
# 백준에서는 sys 모듈로 입력을 받아야 함
# Doc : https://docs.python.org/ko/3/library/heapq.html
# Ref : https://juhee-maeng.tistory.com/94
import heapq

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x: # x가 0이 아닌 숫자
        heapq.heappush(heap, (-1) * x)
    else: # x가 0인 경우
        if len(heap): # 힙이 비어있지 않는 경우
            print((-1)*heapq.heappop(heap))
        else: # 힙이 비어있는 경우
            print(0)