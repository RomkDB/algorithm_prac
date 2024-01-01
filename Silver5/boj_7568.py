# 백준 덩치
n = int(input())
p_list = []

for _ in range(n):
    p_list.append(list(map(int,input().split())))

for i in p_list:
    rank = 1
    for j in p_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')