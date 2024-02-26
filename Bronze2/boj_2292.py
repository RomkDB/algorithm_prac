# 백준 벌집
# 거리 0 : 1
# 거리 1 : 2 ~ 7(6개)
# 거리 2 : 8 ~ 19(12개)
# 거리 3 : 20 ~ 37(18개)
# 1 + (6 * 거리)
n = int(input())
s_point = 1

for i in range(n):
    s_point += i * 6

    if n <= s_point:
        print(i+1)
        break
