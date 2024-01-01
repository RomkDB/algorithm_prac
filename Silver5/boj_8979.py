# 올림픽
n, k = map(int, input().split())
c_list = []

for _ in range(n):
    c_list.append(list(map(int, input().split())))

c_list.sort(key=lambda x : (x[1],x[2],x[3]), reverse=True)

for i in range(n):
    if c_list[i][0] == k:
        index = i

for i in range(n):
    if c_list[index][1:] == c_list[i][1:]:
        print(i + 1)
        break