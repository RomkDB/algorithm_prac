# 백준 2170번 선 긋기
# 입력을 sys.stdin.readline으로 변경하여 제출
n = int(input())
pos_list = []
result = 0

for i in range(n):
    x, y = map(int, input().split())
    pos_list.append((x, y))

pos_list.sort()
start, cur = pos_list[0]

for line in pos_list:
    x, y = line

    if cur >= x:
        cur = max(cur, y)
    else:
        result += cur - start
        start = x
        cur = y

result += cur - start

print(result)