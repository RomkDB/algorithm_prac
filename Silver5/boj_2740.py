# 행렬 곱셈
a = []
b = []

n, m = map(int, input().split())
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for _ in range(m):
    b.append(list(map(int, input().split())))

# n*m  m*k  => n*k
c = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            c[i][j] += a[i][t] * b[t][j]

for r in c:
    for e in r:
        print(e, end=' ')
    print()