# N번째 큰 수
t = int(input())
n = 3

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    print(a[-n])