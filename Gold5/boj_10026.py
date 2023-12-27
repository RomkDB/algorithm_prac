# 백준 적록색약
import sys
sys.setrecursionlimit(100000)

n = int(input())
grid = []
visited = [[False] * n for _ in range(n)]

normal_cnt = 0
rg_cnt = 0

for i in range(n):
    grid.append(list(input()))

def dfs(x, y, color):
    visited[x][y] = True
    direct = [(0,1), (0,-1), (-1,0), (1,0)]
    
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == False:
        # if nx < 0 or nx >= n or ny < 0 or ny >= n:
        #     continue
        # else:
            if grid[nx][ny] == color:
                dfs(nx, ny, color)

# 정상인
for c in ['R', 'G', 'B']:
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and grid[x][y] == c:
                dfs(x, y, c)
                normal_cnt += 1

# 적록색약
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] == 'R'

for c in ['R', 'B']:
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and grid[x][y] == c:
                dfs(x, y, c)
                rg_cnt += 1
                
print(normal_cnt, rg_cnt)