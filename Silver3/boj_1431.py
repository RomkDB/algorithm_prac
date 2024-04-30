# 백준 1431번 시리얼 번호
def digit_sum(num):
    result = 0

    for i in num:
        if i.isdigit():
            result += int(i)
    return result

n = int(input())
num_list = []

for j in range(n):
    num = input()
    num_list.append(num)

num_list.sort(key=lambda x: (len(x), digit_sum(x), x))

for x in num_list:
    print(x)