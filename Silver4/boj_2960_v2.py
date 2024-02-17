# 에라토스테네스의 체
n, k = map(int, input().split())
remove_history = [False] * (n+1)
cnt = 0

# 1번 step
for i in range(2, n+1):
    if remove_history[i] == False:
        # 3번 step
        for j in range(i, n+1, i):
            if remove_history[j] == False:
                remove_history[j] = True
                cnt += 1
                if cnt == k:
                    print(j)