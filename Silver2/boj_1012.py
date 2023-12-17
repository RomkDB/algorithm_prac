# 백준 유기농 배추
# ※ sys.setrecursionlimit
# https://fuzzysound.github.io/sys-setrecursionlimit
# https://kingnamji.tistory.com/39

import sys

sys.setrecursionlimit(100000)
t = int(input())

def dfs(x, y):
    visited[x][y] = True
    direct = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if ground[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        y, x = map(int, input().split())
        ground[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if ground[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)