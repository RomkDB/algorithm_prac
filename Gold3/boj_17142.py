# 백준 17142 연구소 3
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def comb(arr, n):
    if n == 0:
        return [[]]
    
    result = []

    for i in range(len(arr)):
        front = arr[i]

        for back in comb(arr[i+1:], n-1):
            result.append([front] + back)
    
    return result
def bfs(selected):
    global answer
    visited = [[-1] * n for _ in range(n)]
    dq = deque()
    cnt = 0

    for i, j in selected:
        visited[i][j] = 0
        dq.append((i, j))
    
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if visited[nx][ny] == -1 and arr[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                dq.append((nx, ny))

                if arr[nx][ny] == 0:
                    cnt += 1
    max_time = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                max_time = max(max_time, visited[i][j])
    
    if cnt == target:
        answer = min(max_time, answer)

n, m = map(int, input().split())
viruses = []
arr = []
target = 0
answer = int(1e9)

for i in range(n):
    arr.append(list(map(int, input().split())))

    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i, j))
        if arr[i][j] == 0:
            target += 1

combinations = comb(viruses, m)

for selected in combinations:
    bfs(selected)

if answer == int(1e9):
    print(-1)
else:
    print(answer)