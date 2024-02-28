# 백준 숫자 카드 2
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_cnt = Counter(n_list)
answer = []

for i in m_list:
    if i in n_cnt:
        answer.append(str(n_cnt[i]))
    else:
        answer.append('0')

print(' '.join(answer))