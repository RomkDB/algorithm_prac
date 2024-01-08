# 백준 바닥장식
n, m = map(int, input().split())
room = []
cnt = 0

for _ in range(n):
    room.append(list(input())) # [-,-,-,-]
check = [[False]*m for _ in range(n)]

# m = 4 -> [False,False,False,False]

def dfs(x, y):
    check[x][y] = True
    if room[x][y] == '|':
        if x+1 < n and room[x+1][y] == '|' and check[x+1][y] == False:
            dfs(x+1, y)
        else:
            return
    if room[x][y] == '-':
        if y+1 < m and room[x][y+1] == '-' and check[x][y+1] == False:
            dfs(x, y+1)
        else:
            return

for i in range(n):
    for j in range(m):
        if check[i][j] == False:
            dfs(i, j)
            cnt += 1

print(cnt)