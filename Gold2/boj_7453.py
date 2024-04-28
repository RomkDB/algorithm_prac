# 백준 7453번 합이 0인 네 정수
n = int(input())
A, B, C, D = [], [], [], []
count = {}
result = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):
        sum_val = A[i] + B[j]
        
        if sum_val in count:
            count[sum_val] += 1
        else:
            count[sum_val] = 1

for x in range(n):
    for y in range(n):
        sum_val = C[x] + D[y]

        if -sum_val in count:
            result += count[-sum_val]

print(result)