# 백준 생일
n = int(input())
s_list = []

for _ in range(n):
    n, d, m, y = input().split()
    if len(m) == 1:
        m = '0' + m
    if len(d) == 1:
        d = '0' + d
    ymd = y + m + d
    s_list.append([ymd, n])
s_list.sort(reverse=True)

print(s_list[0][1])
print(s_list[-1][1])