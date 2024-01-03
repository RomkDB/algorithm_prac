# 백준 좌표 정렬하기 2
n = int(input())
cor = []

for _ in range(n):
    cor.append(list(map(int,input().split())))

cor.sort(key = lambda x : (x[1], x[0]))

for i in cor:
    print(*i)