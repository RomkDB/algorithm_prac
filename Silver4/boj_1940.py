# 백준 주몽
n = int(input())
m = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
l_point, r_point, cnt = 0, n-1 , 0

while l_point < r_point:
    if n_list[l_point] + n_list[r_point] == m:
        cnt += 1
        l_point += 1
        r_point -= 1
    elif n_list[l_point] + n_list[r_point] < m:
        l_point += 1
    elif n_list[l_point] + n_list[r_point] > m:
        r_point -= 1

print(cnt)