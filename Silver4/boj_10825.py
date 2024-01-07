# 백준 국영수
n = int(input())
s_list = []

for _ in range(n):
    s_list.append(input().split())

s_list.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0])) # -를 붙이면 내림차순(문자열은 불가능)

for i in s_list:
    print(i[0])