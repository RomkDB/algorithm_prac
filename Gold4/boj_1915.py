# 백준 1915번 가장 큰 정사각형
n, m = map(int, input().split())
matrix = [[0 for _ in range(m+1)] for i in range(n+1)]
dp = [[0 for _ in range(m+1)] for i in range(n+1)]

for i in range(n):
    line = list(map(int, list(input())))

    for idx, j in enumerate(line):
        matrix[i+1][idx+1] = j

for x in range(1, n+1):
    for y in range(1, m+1):
        if matrix[x][y]:
            dp[x][y] = min(dp[x-1][y], dp[x-1][y-1], dp[x][y-1]) + 1

print(max([max(k) for k in dp]) ** 2)