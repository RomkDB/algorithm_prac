# 백준 2437번 저울
n = int(input())
weight_list = list(map(int, input().split()))
weight_list.sort()
result = 0

for i in weight_list:
    if i <= result + 1:
        result += i
    else:
        break

print(result + 1)