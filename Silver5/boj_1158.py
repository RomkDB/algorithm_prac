# 요세푸스 문제
from collections import deque

n, k = map(int, input().split())
dq = deque()
answer = []

for i in range(1, n+1):
    dq.append(i)

while len(dq) != 0:
    for _ in range(k-1):
        dq.append(dq.popleft())
    answer.append(dq.popleft())

print('<',end='')
print(', '.join(map(str, answer)), end='') # join은 str 자료형만 가능
print('>')