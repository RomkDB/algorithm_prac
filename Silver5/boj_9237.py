# 백준 9237번 이장님 초대
n = int(input())
grow_day = list(map(int, input().split()))
max_val = 0

grow_day.sort(reverse=True)

for i in range(n):
    max_val = max(max_val, i + 1 + grow_day[i])

print(max_val + 1)