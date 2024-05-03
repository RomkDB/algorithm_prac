# 백준 20057번 마법사 상어와 토네이도
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
left = [
    (-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07),
    (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.1),
    (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)
]
down = [(-y, x, val) for x, y, val in left]
right = [(x, -y, val) for x, y, val in left]
up = [(y, x, val) for x, y, val in left]
move_dir = [left, down, right, up]

def move_state():
    global x, y, direction, turn, move, target
    if move == target:
        move = 0
        turn +=1
        direction = (direction+1) % 4
    if turn == 2:
        turn = 0
        target += 1
    
    x = x + dx[direction]
    y = y + dy[direction]
    move += 1

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))
x = n // 2
y = n // 2
direction = 0
turn = 0
move = 0
target = 1
result = 0
cnt = 1

while cnt < n * n:
    move_state()
    remain = matrix[x][y]

    for i in range(9):
        nx, ny, per = move_dir[direction][i]
        nx += x
        ny += y
        cur = int(matrix[x][y] * per)

        if nx < 0 or nx >=n or ny < 0 or ny >= n:
            result += cur
        else:
            matrix[nx][ny] += cur

        remain -= cur
    
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >=n or ny < 0 or ny >= n:
        result += remain
    else:
        matrix[nx][ny] += remain
    
    matrix[x][y] = 0
    cnt += 1

print(result)