# 백준 회전하는 큐
from collections import deque

n, m = map(int, input().split())
pick_num = list(map(int, input().split()))
dq = deque([x for x in range(1, n+1)])
cnt = 0

for i in pick_num:
    # 뽑으려는 숫자가 dq의 중간지점 이후에 위치한 경우
    # 3번 연산이 최소 횟수 -> rotate(양수)
    if dq.index(i) >= (len(dq)/2):
        k = len(dq) - dq.index(i)
        cnt += k
        dq.rotate(k)
    # 뽑으려는 숫자가 dq의 중간지점 이전에 위치한 경우
    # 2번 연산이 최소 횟수 -> rotate(음수)
    else:
        k = dq.index(i)
        cnt += k
        dq.rotate(-k)
    dq.popleft()
print(cnt)