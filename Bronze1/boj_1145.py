# 백준 적어도 대부분의 배수
n_list = list(map(int, input().split()))
min_n = min(n_list)

while True:
    cnt = 0
    for i in n_list:
        if min_n % i == 0:
            cnt += 1
    if cnt >= 3:
        print(min_n)
        break
    min_n += 1