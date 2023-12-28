# 백준 수들의 합 5
n = int(input())
cnt = 0
sum = 0
start = 0
end = 0

while end <= n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        cnt += 1
        end += 1
        sum += end
print(cnt)