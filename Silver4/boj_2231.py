# 백준 반복수열
a, p = map(int, input().split())
n_list = [a]

while True:
    sum = 0
    for i in str(n_list[-1]):
        sum += int(i) ** p
    if sum in n_list:
        f_num = sum
        break
    n_list.append(sum)

print(len(n_list[:n_list.index(f_num)]))