# 백준 1932번 정수 삼각형
n = int(input())
tri = [[0 for _ in range(n+1)] for i in range(n+1)]
dp = [[0 for _ in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))

    for j in range(1, i+1):
        tri[i][j] = line[j - 1]

for x in range(1, n+1):
    for y in range(1, x+1):
        dp[x][y] = max(dp[x-1][y-1], dp[x-1][y]) + tri[x][y]

print(max(dp[-1]))