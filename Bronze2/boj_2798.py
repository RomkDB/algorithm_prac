# 백준 2798번 블랙잭
# 파이썬은 1초에 2000만정도의 연산을 수행
# 카드 중 3개를 뽑는 경우의 수 = C(n, 3)
# n(n-1)(n-2) / 3! => 약 1,000,000 경우의 수이기 때문에 완전탐색이 가능
n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_val = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_num = cards[i] + cards[j] + cards[k]
            if sum_num <= m and sum_num > max_val:
                max_val = sum_num

print(max_val)

# 다른 풀이
# from itertools import combinations

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# max_val = 0

# for i in combinations(cards, 3):
#     sum_num = sum(i)
#     if sum_num <= m and sum_num > max_val:
#         max_val = sum_num

# print(max_val)