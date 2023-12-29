# 백준 누울 자리를 찾아라
n = int(input())
room = []
r_pos = 0
c_pos = 0

for _ in range(n):
    room.append(list(input()))

for i in range(n):
    r_cnt = 0
    for j in range(n):
        if room[i][j] == '.':
            r_cnt += 1
        else:
            r_cnt = 0
        if r_cnt == 2:
            r_pos += 1

for x in range(n):
    c_cnt = 0
    for y in range(n):
        if room[y][x] == '.':
            c_cnt += 1
        else:
            c_cnt = 0
        if c_cnt == 2:
            c_pos += 1

print(r_pos, c_pos)