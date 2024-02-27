# 풍선 터뜨리기
from collections import deque

n = int(input())
balloon_num = deque(enumerate(map(int, input().split())))
answer = []

while balloon_num:
    idx, num = balloon_num.popleft()
    answer.append(idx + 1)

    if num > 0:
        balloon_num.rotate(-(num-1))
    elif num < 0:
        balloon_num.rotate(-num)

print(' '.join(map(str, answer)))