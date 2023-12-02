# 프로그래머스 주식가격
from collections import deque

def solution(prices):
    dq = deque(prices)
    answer = []
    
    while dq:
        price = dq.popleft()
        second = 0
        for i in dq:
            second += 1
            if price > i:
                break
        answer.append(second)
    
    return answer

print(solution([1,2,3,2,3]))