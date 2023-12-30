# 색종이
coor = [[0]*101 for _ in range(101)]
sum = 0
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            coor[i][j] = 1

for k in coor:
    sum += k.count(1)

print(sum)