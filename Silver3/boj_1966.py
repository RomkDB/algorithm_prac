from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dq = deque(list(map(int, input().split())))
    cnt = 0

    while dq:
        first = max(dq)
        front = dq.popleft()
        m -= 1

        if first == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            dq.append(front)
            if m < 0:
                m = len(dq) - 1