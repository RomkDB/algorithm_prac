# 백준 수학숙제
n = int(input())
n_list = []

for _ in range(n):
    line = input()
    temp = ''

    for i in line:
        if i.isdigit():
            temp += i
        else:
            if temp:
                n_list.append(int(temp))
                temp = ''
    if temp:
        n_list.append(int(temp))

n_list.sort()

for x in n_list:
    print(x)