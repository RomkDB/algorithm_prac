# 백준 1080번 행렬
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]
result = 0

def flip(x, y, a):
    for i in range(3):
        for j in range(3):
            a[x+i][y+j] ^= 1

for i in range(n - 2):
    for j in range(0, m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j, a)
            result += 1

if a != b:
    print(-1)
else:
    print(result)