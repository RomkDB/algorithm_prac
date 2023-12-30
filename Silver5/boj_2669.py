# 백준 직사각형 네개의 합집합의 면적 구하기
coor = [[0]*101 for _ in range(101)]
sum = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            coor[i][j] = 1

for k in coor:
    sum += k.count(1)

print(sum)