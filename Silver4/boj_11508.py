# 백준 2+1 세일
n = int(input())
ksg_list = []
sum = 0

for _ in range(n):
    ksg_list.append(int(input()))

ksg_list.sort(reverse=True)

for i in range(len(ksg_list)):
    if i % 3 != 2:
        sum += ksg_list[i]

print(sum)