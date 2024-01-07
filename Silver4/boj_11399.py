# 백준 ATM
n = int(input())
t_list = list(map(int, input().split()))
sum = 0
temp = 0

t_list.sort()

for i in t_list:
    temp += i
    sum += temp

print(sum)