# 백준 카드2
from collections import deque

n = int(input())
card_dq = deque([i+1 for i in range(n)])

while len(card_dq) != 1:
    card_dq.popleft()
    card_dq.append(card_dq.popleft())

print(card_dq[0])