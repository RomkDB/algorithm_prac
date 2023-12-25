# 백준 일곱 난쟁이
h_list = []
other1 = other2 = 0

for _ in range(9):
    h = int(input())
    h_list.append(h)

for i in h_list:
    for j in h_list:
        if sum(h_list) - i - j == 100 and i != j:
            other1 = i
            other2 = j

h_list.remove(other1)
h_list.remove(other2)
h_list.sort()

for k in h_list:
    print(k)