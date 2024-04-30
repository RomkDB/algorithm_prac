# 백준 11497번 통나무 건너뛰기
t = int(input())

for _ in range(t):
    n = int(input())
    tree_list = list(map(int, input().split()))
    tree_list.sort(reverse=True)

    result = [0] * n
    result[n // 2] = tree_list[0]

    for i in range(1, n):
        if i % 2 == 1:
            result[n // 2 - i // 2 - 1] = tree_list[i]
        else:
            result[n // 2 + i // 2] = tree_list[i]

    max_dif = 0

    for j in range(n):
        dif = abs(result[j] - result[(j + 1) % n])
        max_dif = max(max_dif, dif)
    
    print(max_dif)