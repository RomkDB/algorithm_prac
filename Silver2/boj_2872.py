# 백준 2872번 우리집엔 도서관이 있어
# 입력 크기 때문에 sys.stdin.readline으로 제출
n = int(input())
b_num = []
max_val = 0
max_idx = -1

for _ in range(1, n+1):
    b_num.append(int(input()))

for i in range(n):
    if max_val < b_num[i]:
        max_val = b_num[i]
        max_idx = i

length = 1
target = max_val - 1

for j in range(max_idx - 1, -1, -1):
    if target == b_num[j]:
        target -= 1
        length += 1

print(n - length)