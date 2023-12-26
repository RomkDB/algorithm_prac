# 백준 단지번호붙이기

n = int(input())
sq_map = []
visited = [[False] * n for _ in range(n)]
group_list = []
cnt = 1

for _ in range(n):
    sq_map.append(list(map(int,input())))

def dfs(x, y):
    global cnt
    visited[x][y] = True
    direct = [(0,1), (0,-1), (-1,0), (1,0)]
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if sq_map[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)
            cnt += 1

for i in range(n):
    for j in range(n):
        if sq_map[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            # if cnt != 1:
            group_list.append(cnt)
            cnt = 1
            
group_list.sort()
print(len(group_list))
for i in group_list:
    print(i)